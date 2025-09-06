import requests
import json

url = "http://127.0.0.1:8000/predict"
data = {
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

response = requests.post(url, json=data)
print(json.dumps(response.json(), indent=2))

