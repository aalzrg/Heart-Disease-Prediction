from fastapi import APIRouter, HTTPException
from backend.schemas.patient import PatientData
from backend.services.model import predict_heart_disease_service
import json
import os
from datetime import datetime

router = APIRouter()

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

        # Append to log file
        os.makedirs("logs", exist_ok=True)
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as f:
                json.dump([], f)

        with open(LOG_FILE, "r+") as f:
            data = json.load(f)
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=2)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
