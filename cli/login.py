# cli/login.py

from rich.console import Console
from rich.prompt import Prompt

console = Console()

# Hardcoded demo account
VALID_USER = {
    "admin": "demo123"
}

def login():
    """
    Simple login system: asks for username/password repeatedly until successful.
    Returns True when login is successful.
    """
    console.print("\n[bold cyan]Please login to continue:[/bold cyan]\n")

    while True:
        username = Prompt.ask("[bold yellow]Username[/bold yellow]")
        password = Prompt.ask("[bold yellow]Password[/bold yellow]", password=True)

        if username in VALID_USER and VALID_USER[username] == password:
            console.print("[bold green]✅ Login successful! Welcome.[/bold green]\n")
            return True
        else:
            console.print("[bold red]❌ Invalid username or password. Please try again.[/bold red]\n")
