from fastapi import APIRouter, HTTPException 
from backend.schemas.patient import PatientData                # fixed
from backend.services.model import predict_heart_disease_service  # fixed


router = APIRouter()

@router.post("/predict")
def predict_heart_disease(patient: PatientData):
    try:
        return predict_heart_disease_service(patient)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
