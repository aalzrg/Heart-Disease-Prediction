# cli/commands/predict.py

import json
from pathlib import Path
from rich.console import Console
from rich.prompt import IntPrompt, FloatPrompt
from cli.commands.utils import send_prediction_request

console = Console()
STORAGE_DIR = Path("cli/user_data")
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

# Hardcoded demo user (for this demo)
CURRENT_USER = "admin"

# Feature validation ranges
FEATURE_RANGES = {
    "age": (18, 110),
    "sex": (0, 1),
    "cp": (0, 3),
    "trestbps": (50, 250),
    "chol": (100, 600),
    "fbs": (0, 1),
    "restecg": (0, 2),
    "thalach": (60, 220),
    "exang": (0, 1),
    "oldpeak": (0.0, 10.0),
    "slope": (0, 2),
    "ca": (0, 3),
    "thal": (1, 3)
}

def ask_int(feature, min_val, max_val):
    while True:
        value = IntPrompt.ask(f"{feature} [{min_val}-{max_val}]")
        if min_val <= value <= max_val:
            return value
        console.print(f"[bold red]Invalid value! Must be between {min_val}-{max_val}[/bold red]")

def ask_float(feature, min_val, max_val):
    while True:
        value = FloatPrompt.ask(f"{feature} [{min_val}-{max_val}]")
        if min_val <= value <= max_val:
            return value
        console.print(f"[bold red]Invalid value! Must be between {min_val}-{max_val}[/bold red]")

def run_predict():
    """Guided input for a single patient and prediction"""
    console.print("\n[bold cyan]Enter patient features:[/bold cyan]\n")

    try:
        patient_data = {
            "age": ask_int("Age", *FEATURE_RANGES["age"]),
            "sex": ask_int("Sex (0=female,1=male)", *FEATURE_RANGES["sex"]),
            "cp": ask_int("Chest Pain Type (0-3)", *FEATURE_RANGES["cp"]),
            "trestbps": ask_int("Resting Blood Pressure", *FEATURE_RANGES["trestbps"]),
            "chol": ask_int("Cholesterol", *FEATURE_RANGES["chol"]),
            "fbs": ask_int("Fasting Blood Sugar > 120mg/dl (0/1)", *FEATURE_RANGES["fbs"]),
            "restecg": ask_int("Resting ECG (0-2)", *FEATURE_RANGES["restecg"]),
            "thalach": ask_int("Max Heart Rate Achieved", *FEATURE_RANGES["thalach"]),
            "exang": ask_int("Exercise Induced Angina (0/1)", *FEATURE_RANGES["exang"]),
            "oldpeak": ask_float("Oldpeak (ST depression)", *FEATURE_RANGES["oldpeak"]),
            "slope": ask_int("Slope of ST segment (0-2)", *FEATURE_RANGES["slope"]),
            "ca": ask_int("Number of major vessels colored by fluoroscopy (0-3)", *FEATURE_RANGES["ca"]),
            "thal": ask_int("Thalassemia (1=normal,2=fixed defect,3=reversible defect)", *FEATURE_RANGES["thal"])
        }

        # Use utils helper for API call
        result = send_prediction_request(patient_data)

        if result:
            prediction = result["prediction"]
            probability = result["probability"]

            console.print("\n[bold green]✅ Prediction Result:[/bold green]")
            console.print(f"[bold yellow]Heart Disease:[/bold yellow] {'Yes' if prediction == 1 else 'No'}")
            console.print(f"[bold cyan]Probability:[/bold cyan] {probability}\n")

            # --- Persist result for the current user ---
            user_file = STORAGE_DIR / f"{CURRENT_USER}.json"
            if user_file.exists():
                data = json.loads(user_file.read_text())
            else:
                data = []

            data.append({
                "features": patient_data,
                "prediction": prediction,
                "probability": probability,
                "method": "manual"   # ✅ mark as manual prediction
            })

            user_file.write_text(json.dumps(data, indent=2))
            return prediction

        else:
            return None

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return None
