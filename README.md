# passgen-cli

A simple and secure command-line password generator built with Python.

## Features

- Generate cryptographically secure random passwords
- Customizable password length
- Beautiful terminal output with Rich library
- Uses lowercase, uppercase, digits, and special characters

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Generate a password with default length (16 characters):

```bash
python app.py
```

### Custom Length

```bash
python app.py --length 20
python app.py -l 20
```

### Version Information

```bash
python app.py --version
```

## Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--length` | `-l` | Password length | 16 |
| `--version` | | Show version and exit | - |

