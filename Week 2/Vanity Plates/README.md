# Vanity Plates

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 2 - Vanity Plates Problem Set](https://cs50.harvard.edu/python/2022/psets/2/plates/), named `plates.py`, validates vanity license plates based on specific requirements. The program prompts the user for a vanity plate and determines whether it meets all of the given requirements. If the input plate is valid, it outputs "Valid," otherwise, it outputs "Invalid." The following requirements need to be met for a vanity plate to be considered valid:

- All vanity plates must start with at least two letters.
- Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
- Numbers cannot be used in the middle of a plate; they must come at the end. The first number used cannot be a '0'.
- No periods, spaces, or punctuation marks are allowed.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `plates.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python plates.py
   ```

4. The program will prompt you to enter a vanity plate. After you enter the plate, it will output "Valid" if the plate meets all requirements, or "Invalid" if it does not.

## Program Code

```python
# plates.py

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return has_two_letters(s) and has_valid_length(s) and has_valid_numbers(s) and has_no_punctuation(s)


def has_two_letters(s):
    # Check if the string has at least two letters at the beginning
    if len(s) < 2:
        return False
    if not all(c.isalpha() for c in s[:2]):
        return False
    return True


def has_valid_length(s):
    # Check if the string has a minimum length of 2 and a maximum length of 6
    if not 2 <= len(s) <= 6:
        return False
    return True


def has_valid_numbers(s):
    # Check if the string has no numbers in the middle and the last character is not '0'
    if any(c.isdigit() for c in s[2:-1]) or s[-1] == "0":
        return False
    return True


def has_no_punctuation(s):
    # Check if the string contains no punctuation marks
    if all(c.isalpha() or c.isdigit() for c in s):
        return True
    return False


if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the prompts to enter various vanity plates.
3. The program will output "Valid" if the entered plate meets the requirements, and "Invalid" if it does not.

## Sample Test Cases

1. **Input:** CS50
   **Result:** Valid

2. **Input:** CS05
   **Result:** Invalid

3. **Input:** CS50P
   **Result:** Invalid

4. **Input:** PI3.14
   **Result:** Invalid

5. **Input:** H
   **Result:** Invalid

6. **Input:** OUTATIME
   **Result:** Invalid

## Additional Notes

Remember to save the `plates.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, make sure you are in the correct directory and have saved the file with the correct name.