import re
import getpass


def analyze_password(password):
    """Return a basic strength label and suggestions for improvement."""
    score = 0
    suggestions = []

    checks = [
        (len(password) >= 8, "Use at least 8 characters."),
        (bool(re.search(r"[A-Z]", password)), "Add an uppercase letter."),
        (bool(re.search(r"[a-z]", password)), "Add a lowercase letter."),
        (bool(re.search(r"\d", password)), "Add a number."),
        (bool(re.search(r"[^A-Za-z0-9]", password)), "Add a special character."),
    ]

    for passed, suggestion in checks:
        if passed:
            score += 1
        else:
            suggestions.append(suggestion)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions


def main():
    print("=== Password Strength Analyzer ===")
    password = getpass.getpass("Enter a test password (input is hidden): ")

    strength, suggestions = analyze_password(password)
    print(f"\nPassword strength: {strength}")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("All basic complexity checks passed.")

    print("\nEducational note: This is a basic complexity checker, not a guarantee")
    print("that a password is secure. Never test with a password you actually use.")


if __name__ == "__main__":
    main()
