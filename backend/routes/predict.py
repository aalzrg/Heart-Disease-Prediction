from fastapi import APIRouter, HTTPException
from backend.schemas.patient import PatientData
from backend.services.model import predict_heart_disease_service
import json
import os
from datetime import datetime

router = APIRouter()

# Use /tmp for logs (since cli/user_data is read-only on Render)
LOG_FILE = "/tmp/admin.json"

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

        # Initialize file if it doesn’t exist
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                json.dump([], f)

        # Append log entry safely
        with open(LOG_FILE, "r+", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

        return result

    except Exception as e:
        print(f"[ERROR] Prediction failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
