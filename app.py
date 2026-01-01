import string
import secrets

import click
from rich.console import Console
from rich.panel import Panel

console = Console()

# Define password generation methods
DEFAULT_CHARSET = (
    string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
)

MIN_LENGTH = 8
VERSION = "1.0.0"


# Generate a random password with specified length and character set
def generate_password(length: int, charset: str = DEFAULT_CHARSET) -> str:
    if length <= MIN_LENGTH:
        raise ValueError(f"Password length must be greater than {MIN_LENGTH}")

    if not charset:
        raise ValueError("Character set cannot be empty")

    return "".join(secrets.choice(charset) for _ in range(length))


# CLI command definition with options
@click.command()
@click.option(
    "--length",
    "-l",
    type=int,
    default=16,
    show_default=True,
    help="Length of generated password",
)
@click.option(
    "--version",
    is_flag=True,
    help="Show version information and exit",
)
def main(length: int, version: bool):
    if version:
        console.print(f"passgen-cli version {VERSION}")
        raise SystemExit(0)

    try:
        password = generate_password(length)
    except ValueError as e:
        console.log(f"[red]Error: {e}[/red]")
        raise SystemExit(1)

    # Display the generated password in a panel
    panel = Panel.fit(
        f"[bold cyan]{password}[/bold cyan]",
        title="Generated Password",
        border_style="green",
    )

    console.print(panel)


if __name__ == "__main__":
    main()
