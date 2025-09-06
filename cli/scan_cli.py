# cli/scan_cli.py

import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description="Heart Disease Prediction CLI")

    # Add arguments matching your API inputs
    parser.add_argument("--age", type=int, required=True)
    parser.add_argument("--sex", type=int, required=True)
    parser.add_argument("--cp", type=int, required=True)
    parser.add_argument("--trestbps", type=int, required=True)
    parser.add_argument("--chol", type=int, required=True)
    parser.add_argument("--fbs", type=int, required=True)
    parser.add_argument("--restecg", type=int, required=True)
    parser.add_argument("--thalach", type=int, required=True)
    parser.add_argument("--exang", type=int, required=True)
    parser.add_argument("--oldpeak", type=float, required=True)
    parser.add_argument("--slope", type=int, required=True)
    parser.add_argument("--ca", type=int, required=True)
    parser.add_argument("--thal", type=int, required=True)

    args = parser.parse_args()

    # Convert parsed args to dict
    payload = vars(args)

    # The URL to your running FastAPI backend
    url = "http://api:8000/predict"


    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            prediction = result.get("prediction")
            probability = result.get("probability")
            print("\nPrediction: ", "Heart Disease" if prediction == 1 else "No Heart Disease")
            print("Probability:", probability)
        else:
            print(f"API Error {response.status_code}: {response.text}")
    except Exception as e:
        print("Failed to connect to API:", e)

if __name__ == "__main__":
    main()
