import sys


def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0

    while True:
        try:
            item = input("Item: ")
            if item.capitalize() or item.title() in menu:
                for dish in menu:
                    if item.capitalize() == dish or item.title() == dish:
                        total +=  menu[dish]
                        print(f"Total: ${total:.2f}")
        except EOFError:
            break


if __name__ == "__main__":
    main()