import os
import joblib
import pandas as pd
from backend.schemas.patient import PatientData                # fixed


# Fix BASE_DIR to point to Demo root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # backend/services/model.py -> Demo/

model_path = os.path.join(BASE_DIR, "model", "heart_model.pkl")
scaler_path = os.path.join(BASE_DIR, "model", "heart_scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def predict_heart_disease_service(patient: PatientData):
    patient_df = pd.DataFrame([patient.dict()])
    patient_scaled = scaler.transform(patient_df)
    prediction = model.predict(patient_scaled)[0]
    probability = model.predict_proba(patient_scaled)[0].tolist()
    
    return {
        "prediction": int(prediction),
        "probability": probability
    }
