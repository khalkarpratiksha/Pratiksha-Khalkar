def check_password_strength(password):
    """Checks the strength of a password against predefined criteria.

    Args:
        password: The password string to check.

    Returns:
        A dictionary indicating whether each criterion is met (True/False).
    """

    criteria = {
        "Length (> 8)": len(password) > 8,
        "Uppercase Letter": any(char.isupper() for char in password),
        "Lowercase Letter": any(char.islower() for char in password),
        "Number": any(char.isdigit() for char in password),
        "Special Character": any(char in "!@#$%^&*()-+" for char in password)
    }
    return criteria


def main():
    while True:
        password = input("Enter your password: ")
        criteria = check_password_strength(password)

        if all(criteria.values()):
            print("Strong Password!")
            break
        else:
            print("Password could be stronger:")
            for key, value in criteria.items():
                if not value:
                    print(f"- {key}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
