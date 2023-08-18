import validators


def main():
    print(validate_email(input("What's your email address? ").strip()))


def validate_email(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()