import sys


def main():
    groceries = []
    fruits = {}

    while True:
        try:
            item = input()
            groceries.append(item)
            count = 0
            for grocery in groceries:
                if item == grocery:
                    count += 1
                fruits.update({
                    item: count
                })
        except EOFError:
            print()
            for fruit in sorted(fruits):
                print(fruits[fruit], fruit.upper())
            break


if __name__ == "__main__":
    main()