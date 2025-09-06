#!/usr/bin/env python3

import sys
from rich.console import Console
from cli.cli_shell import run_cli
from cli.banner import show_banner

console = Console()

def main():
    console.clear()
    show_banner()  # Show ASCII banner at start
    try:
        run_cli()  # Start interactive CLI loop
    except KeyboardInterrupt:
        console.print("\n[bold red] Exiting... Stay healthy ❤️[/bold red]")
        sys.exit(0)


if __name__ == "__main__":
    main()
