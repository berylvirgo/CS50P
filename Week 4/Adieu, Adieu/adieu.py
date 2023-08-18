import sys
import inflect


def main():
    names = []
    p = inflect.engine()

    while True:
        try:
            n = input("Name: ")
            names.append(n)
        except EOFError:
            print()
            print(f"Adieu, adieu, to", p.join(names))
            break


if __name__ == "__main__":
    main()