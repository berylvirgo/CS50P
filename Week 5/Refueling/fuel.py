def main():
    while True:
        try:
            fuel = gauge(convert(input("Fraction: ")))
            print(fuel)
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid fraction.")


def convert(fraction):
    X, Y = fraction.split("/")
    if not X.isdigit() or not Y.isdigit():
        raise ValueError
    if int(Y) == 0:
        raise ZeroDivisionError
    if int(X) > int(Y):
        raise ValueError
    return round(100 * int(X) / int(Y))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()