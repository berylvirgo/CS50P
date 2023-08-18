# Pizza Py

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 6 - Pizza Py Problem Set](https://cs50.harvard.edu/python/2022/psets/6/pizza/). The `pizza.py` program reads a CSV file containing pizza menu items and prices and displays the menu in the form of an ASCII art table using the `tabulate` package.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `pizza.py` file.

   ```
   cd path/to/your/directory
   ```

3. Install the `tabulate` package if you haven't already:

   ```
   pip install tabulate
   ```

4. Run the program using the `python` command and provide the filename of the CSV file as an argument:

   ```
   python pizza.py filename.csv
   ```

   Replace `filename.csv` with the actual name of the CSV file you want to display as a menu.

## Program Code

### pizza.py

```python
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
```

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `pizza.py` program.
2. Provide the name of a CSV file containing the pizza menu (e.g., [sicilian.csv](https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv) or [regular.csv](https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv)) as a command-line argument.
3. The program will display the menu in the form of an ASCII art table.
   ```
   +-----------------+---------+---------+
   | Regular Pizza   | Small   | Large   |
   +=================+=========+=========+
   | Cheese          | $13.50  | $18.95  |
   +-----------------+---------+---------+
   | 1 topping       | $14.75  | $20.95  |
   +-----------------+---------+---------+
   | 2 toppings      | $15.95  | $22.95  |
   +-----------------+---------+---------+
   | 3 toppings      | $16.95  | $24.95  |
   +-----------------+---------+---------+
   | Special         | $18.50  | $26.95  |
   +-----------------+---------+---------+
   ```

## Additional Notes

- The `pizza.py` program reads the CSV file specified in the command-line argument using the `csv` module.
- It uses the `tabulate` package to format the menu items and prices into an ASCII art table.
- The program performs error handling to handle cases where the user provides incorrect command-line arguments or the specified file does not exist.
- After running the program, it will display the menu in the form of an ASCII art table.