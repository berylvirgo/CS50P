import sys
import csv

from tabulate import tabulate


def main():
    print(table())


def table():
    menus = []
    if len(sys.argv) == 2:
        if sys.argv[1].endswith('.csv'):
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.reader(file)
                    for row in reader:
                        menus.append(row)
                    return tabulate(menus[1:], headers=menus[0], tablefmt="grid")
            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a CSV file')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Too few command-line arguments')


if __name__ == "__main__":
    main()