# Password Strength Analyzer

A beginner-friendly Python project for the Thiranex internship task. It checks a password against five basic complexity rules and prints suggestions.

## Features

- Checks minimum length (8 characters)
- Checks for uppercase and lowercase letters
- Checks for digits and special characters
- Labels the result Weak, Moderate, or Strong
- Gives suggestions for missing criteria
- Hides typed input using Python's built-in `getpass` module
- Uses only Python's standard library

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Run

```bash
python3 main.py
```

Use a made-up test password, not a password you use for any real account.

## Project files

- `main.py` — application source code
- `requirements.txt` — no external dependencies are needed

## Limitations

This is a simple educational checker. It does not check breached-password databases, estimate entropy rigorously, or guarantee password security. A strong passphrase and a password manager are generally preferable to relying only on character variety.
