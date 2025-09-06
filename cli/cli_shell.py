# cli/cli_shell.py

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import HTML
from rich.console import Console
from rich.table import Table
from cli.login import login
from cli.banner import show_banner
from cli.commands import predict, loaddetect, stats

console = Console()

# Available commands
COMMANDS = ["help", "predict", "loaddetect", "stats", "clear", "exit"]
completer = WordCompleter(COMMANDS, ignore_case=True)


def show_help():
    console.print("\n[bold cyan]Available Commands:[/bold cyan]")
    console.print("[bold green]predict[/bold green]     - Enter patient features one by one")
    console.print("[bold green]loaddetect[/bold green] - Load patients from a CSV file and predict all")
    console.print("[bold green]stats[/bold green]       - Show summary of tested patients")
    console.print("[bold green]clear[/bold green]       - Clear the screen")
    console.print("[bold green]exit[/bold green]        - Quit the CLI\n")


def run_cli():
    """Main CLI loop"""
    # Login first
    if not login():
        return

    # Show banner
    show_banner()

    # Initialize prompt session
    session = PromptSession()
    
    # Store stats (simple in-memory for demo)
    cli_stats = {
        "total": 0,
        "heart_disease": 0,
        "no_heart_disease": 0
    }

    while True:
        try:
            user_input = session.prompt(
                HTML('<ansired>heart-demo&gt; </ansired>'), 
                completer=completer
            ).strip().lower()

            if user_input == "help":
                show_help()

            elif user_input == "predict":
                result = predict.run_predict()
                if result is not None:
                    cli_stats["total"] += 1
                    if result == 1:
                        cli_stats["heart_disease"] += 1
                    else:
                        cli_stats["no_heart_disease"] += 1

            elif user_input.startswith("loaddetect"):
                parts = user_input.split(maxsplit=1)
                if len(parts) != 2:
                    console.print("[bold red]Usage: loaddetect filename.csv[/bold red]")
                else:
                    filename = parts[1].strip('"')
                    loaddetect.loaddetect(filename)

            elif user_input == "stats":
                stats.show_stats()

            elif user_input == "clear":
                console.clear()

            elif user_input == "exit":
                console.print("[bold cyan]👋 Goodbye! Stay healthy![/bold cyan]")
                break

            elif user_input == "":
                continue

            else:
                console.print(f"[bold red]Unknown command:[/bold red] {user_input}")
                console.print("Type [bold green]help[/bold green] to see available commands.\n")

        except KeyboardInterrupt:
            console.print("\n[bold cyan]Use 'exit' to quit the CLI.[/bold cyan]\n")
        except EOFError:
            console.print("\n[bold cyan]Exiting CLI...[/bold cyan]")
            break
