import os
import joblib
from feature_input import get_sample_patient

# ✅ Automatically find the base project directory (no more ../ issues)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ✅ Full path to model and scaler
model_path = os.path.join(BASE_DIR, "model", "heart_model.pkl")
scaler_path = os.path.join(BASE_DIR, "model", "heart_scaler.pkl")

# ✅ Load model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# ✅ Get simulated patient input
new_patient = get_sample_patient()

# ✅ Preprocess and predict
new_patient_scaled = scaler.transform(new_patient)
prediction = model.predict(new_patient_scaled)
prob = model.predict_proba(new_patient_scaled)

# print("Prediction (0 = No Heart Disease, 1 = Heart Disease):", prediction[0])
# print("Probability:", prob[0])

from colorama import Fore, Style

prediction_label = "Heart Disease Present" if prediction[0] == 1 else "No Heart Disease"
prob_no = prob[0][0]
prob_yes = prob[0][1]

print("\n--- Model Prediction ---")
if prediction[0] == 1:
    print(Fore.RED + f"Prediction: {prediction_label}" + Style.RESET_ALL)
else:
    print(Fore.GREEN + f"Prediction: {prediction_label}" + Style.RESET_ALL)
print(f"Confidence: {prob_yes*100:.2f}% chance of Heart Disease")
print(f"             {prob_no*100:.2f}% chance of No Heart Disease")
print("-----------------------\n")

