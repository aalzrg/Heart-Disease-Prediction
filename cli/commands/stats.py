# cli/commands/stats.py

import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()
STORAGE_DIR = Path("cli/user_data")
STORAGE_DIR.mkdir(exist_ok=True)
CURRENT_USER = "admin"

def show_stats():
    """
    Display a summary of predictions for the current user.
    Tracks manual predictions and batch CSV predictions separately.
    """
    user_file = STORAGE_DIR / f"{CURRENT_USER}.json"
    if not user_file.exists():
        console.print("[bold yellow]No predictions found for this user yet.[/bold yellow]")
        return

    try:
        data = json.loads(user_file.read_text())
    except json.JSONDecodeError:
        console.print("[bold red]Error reading user data file.[/bold red]")
        return

    # Separate manual vs batch
    manual_data = [d for d in data if d.get("method") == "manual"]
    batch_data = [d for d in data if d.get("method") == "batch"]

    total_manual = len(manual_data)
    total_batch = len(batch_data)
    total = total_manual + total_batch

    heart_manual = sum(1 for d in manual_data if d["prediction"] == 1)
    heart_batch = sum(1 for d in batch_data if d["prediction"] == 1)
    heart_total = heart_manual + heart_batch
    no_heart_total = total - heart_total

    heart_pct = (heart_total / total) * 100 if total else 0
    no_heart_pct = (no_heart_total / total) * 100 if total else 0

    table = Table(title=f"{CURRENT_USER} - Prediction Summary")
    table.add_column("Metric", justify="left")
    table.add_column("Count", justify="right")
    table.add_column("Percentage", justify="right")

    table.add_row("Total Patients Tested (All)", str(total), "100%" if total else "0%")
    table.add_row("  - Manual Predictions", str(total_manual), f"{(total_manual/total*100):.2f}%" if total else "0%")
    table.add_row("  - CSV Batch Predictions", str(total_batch), f"{(total_batch/total*100):.2f}%" if total else "0%")
    table.add_row("Heart Disease (All)", str(heart_total), f"{heart_pct:.2f}%")
    table.add_row("No Heart Disease (All)", str(no_heart_total), f"{no_heart_pct:.2f}%")

    # Optional: highlight if more than half of patients have heart disease
    if total and heart_pct > 50:
        console.print("[bold red]⚠️ High heart disease ratio detected![/bold red]")

    console.print(table)
