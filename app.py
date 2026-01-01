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


# Generate a random password with specified length and character set
def generate_password(length: int, charset: str = DEFAULT_CHARSET) -> str:
    if length <= 0:
        raise ValueError("The length must be 1 or greater")

    return "".join(secrets.choice(charset) for _ in range(length))
