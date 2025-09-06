from fastapi import APIRouter, HTTPException
from backend.schemas.patient import PatientData
from backend.services.model import predict_heart_disease_service
import json
import os
from datetime import datetime

router = APIRouter()

# Define log file path
LOG_FILE = os.path.join("logs", "patient_logs.json")

@router.post("/predict")
def predict_heart_disease(patient: PatientData):
    try:
        # Run prediction
        result = predict_heart_disease_service(patient)

        # Prepare log entry
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": patient.dict(),
            "result": result,
        }

        # Ensure logs folder exists
        os.makedirs("logs", exist_ok=True)

        # Initialize file if it doesn’t exist
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as f:
                json.dump([], f)

        # Append log entry safely
        with open(LOG_FILE, "r+", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []  # reset if file is corrupted
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

        return result

    except Exception as e:
        print(f"[ERROR] Prediction failed: {e}")  # log in Render console
        raise HTTPException(status_code=500, detail=str(e))
