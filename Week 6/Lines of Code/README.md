# Lines of Code

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 6 - Lines of Code Problem Set](https://cs50.harvard.edu/python/2022/psets/6/lines/). The `lines.py` program takes the name of a Python file as a command-line argument and outputs the number of lines of code in that file, excluding comments and blank lines.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `lines.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the `python` command and provide the filename as an argument:

   ```
   python lines.py filename.py
   ```

   Replace `filename.py` with the actual name of the Python file you want to analyze.

## Program Code

### lines.py

```python
import sys

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    # Check if the filename ends with .py
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            code_lines = count_code_lines(file)
            print(f"Number of lines of code in {filename}: {code_lines}")
    except FileNotFoundError:
        sys.exit("File does not exist")

def count_code_lines(file):
    code_lines = 0
    in_comment = False

    for line in file:
        stripped_line = line.strip()

        # Skip blank lines
        if not stripped_line:
            continue

        # Skip comment lines
        if stripped_line.startswith("#"):
            continue

        # Handle multi-line comments
        if stripped_line.startswith("'''") or stripped_line.startswith('"""'):
            in_comment = not in_comment

        if not in_comment:
            code_lines += 1

    return code_lines

if __name__ == "__main__":
    main()
```

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `lines.py` program.
2. Provide the name of a Python file that you want to analyze (e.g., `hello.py`) as a command-line argument.
3. The program will output the number of lines of code in the specified file, excluding comments and blank lines.

## Additional Notes

- The `lines.py` program uses the `sys` module to handle command-line arguments and exit the program if necessary.
- The program also handles different cases of comments, including multi-line comments enclosed in triple quotes (`'''` or `"""`).
- The `count_code_lines` function counts the lines of code in the provided file, excluding comments and blank lines.
- After running the program, it will display the count of code lines in the specified Python file.