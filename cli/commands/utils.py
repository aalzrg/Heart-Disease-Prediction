# cli/commands/utils.py
import os
import requests
from rich.console import Console

console = Console()

# The only API URL: get from env variable (works in Docker)
API_URL = os.environ.get("API_URL", "http://127.0.0.1:8000/predict")

def send_prediction_request(patient_data):
    try:
        response = requests.post(API_URL, json=patient_data)
        if response.status_code == 200:
            return response.json()
        else:
            console.print(f"[bold red]Backend error {response.status_code}:[/bold red] {response.text}")
            return None
    except Exception as e:
        console.print(f"[bold red]Request failed:[/bold red] {e}")
        return None
