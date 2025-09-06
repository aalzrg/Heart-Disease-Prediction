# cli/commands/loaddetect.py

import os
import pandas as pd
import random
from pathlib import Path
from rich.console import Console
from cli.commands.utils import send_prediction_request  # optional if you want real API

console = Console()
STORAGE_DIR = Path("cli/user_data")
STORAGE_DIR.mkdir(exist_ok=True)

CURRENT_USER = "admin"
patients = None  # global patients storage

def loaddetect(filename):
    """
    Load CSV from user's computer, simulate or send detection,
    store each patient result for stats tracking.
    """
    global patients

    if not os.path.isfile(filename):
        console.print(f"[bold red]❌ Error:[/bold red] File '{filename}' does not exist.")
        return

    if not filename.endswith(".csv"):
        console.print("[bold red]❌ Error: Only .csv files are supported.[/bold red]")
        return

    try:
        patients = pd.read_csv(filename)
        count = len(patients)
        console.print(f"[bold green]✅ Successfully loaded {count} patients from {filename}[/bold green]\n")

        # Load existing user data
        user_file = STORAGE_DIR / f"{CURRENT_USER}.json"
        if user_file.exists():
            data = pd.read_json(user_file, orient="records").to_dict(orient="records")
        else:
            data = []

        # Simulate detection for each patient
        console.print("[bold cyan]📊 Detection Results:[/bold cyan]")
        console.print("----------------------------")
        console.print("Index | Heart Disease | Probability (%)")
        console.print("----------------------------")
        for i in range(count):
            # You can replace this with real API: send_prediction_request(patients.iloc[i].to_dict())
            prediction = random.choice([0, 1])
            probability = random.randint(70, 100)
            console.print(f"{i:<5} | {'Yes' if prediction == 1 else 'No':<12} | {probability}%")

            # Append to user file
            data.append({
                "features": patients.iloc[i].to_dict(),
                "prediction": prediction,
                "probability": probability,
                "method": "batch"
            })

        console.print("----------------------------\n")

        # Save updated data
        import json
        user_file.write_text(json.dumps(data, indent=2))

    except Exception as e:
        console.print(f"[bold red]❌ Error loading CSV:[/bold red] {e}")
