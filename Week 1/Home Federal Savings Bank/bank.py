def greeting():
    greet = input("Greeting: ")
    greet = greet.strip().casefold()

    if greet.startswith("h"):
        if greet.startswith("hello"):
            return "$0"
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    print(greeting())