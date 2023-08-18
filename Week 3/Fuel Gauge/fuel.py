def main():
    while True:
        try:
            X, Y = input("Fraction: ").split("/")
            if not X.isdigit() or not Y.isdigit():
                raise ValueError
            if int(Y) == 0:
                raise ZeroDivisionError
            if int(X) > int(Y):
                raise ValueError
            percentage = round(100 * int(X) / int(Y))
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            print("Invalid fraction.")


if __name__ == "__main__":
    main()