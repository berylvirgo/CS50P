def main():
    print(f"${value(input('Greeting: '))}")


def value(greeting):
    greeting = greeting.strip().casefold()

    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            return "0"
        return "20"
    else:
        return "100"


if __name__ == "__main__":
    main()