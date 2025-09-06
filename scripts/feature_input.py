import pandas as pd

def get_sample_patient():
    """
    Simulate a new patient input.
    Features order must match training data columns.
    """
    patient_data = {
        "age": 58,
        "sex": 1,
        "cp": 2,
        "trestbps": 140,
        "chol": 240,
        "fbs": 0,
        "restecg": 1,
        "thalach": 150,
        "exang": 0,
        "oldpeak": 1.5,
        "slope": 2,
        "ca": 0,
        "thal": 2
    }
    df = pd.DataFrame([patient_data])
    return df
