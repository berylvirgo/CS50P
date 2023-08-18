# Fuel Gauge

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 3 - Fuel Gauge Problem Set](https://cs50.harvard.edu/python/2022/psets/3/fuel/), named `fuel.py`, calculates the fuel level in a tank based on a given fraction. It prompts the user to input a fraction in the format X/Y, where X and Y are integers. The program then outputs the fuel level as a percentage, rounded to the nearest integer. If the fuel level is 1% or less, it outputs "E" to indicate that the tank is essentially empty. If the fuel level is 99% or more, it outputs "F" to indicate that the tank is essentially full.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `fuel.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python fuel.py
   ```

4. The program will prompt you to enter a fraction in the format X/Y. After you enter the fraction, it will output the fuel level as a percentage or "E" or "F" based on the calculation.

## Program Code

```python
# fuel.py

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
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the prompts to enter various fractions. Make sure to test cases where the fraction is within the range of 1-99, as well as cases where the fraction results in an "E" or "F" output.
3. The program will output the fuel level as a percentage or "E" or "F" based on the input fraction. If the input is not valid (not in the format X/Y, X or Y not an integer, Y is 0, X is greater than Y), the program will display an "Invalid fraction" message.

## Sample Test Cases

1. **Input:** 3/4
   **Result:** 75%

2. **Input:** 1/4
   **Result:** 25%

3. **Input:** 4/4
   **Result:** F

4. **Input:** 0/4
   **Result:** E

## Additional Notes

Make sure to save the `fuel.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.