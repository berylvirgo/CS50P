# Refueling

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 5 - Refueling Problem Set](https://cs50.harvard.edu/python/2022/psets/5/test_fuel/). The `fuel.py` program calculates the fuel gauge reading based on a given fraction input and provides the corresponding gauge reading using the `convert` and `gauge` functions. The `convert` function calculates the percentage representation of the given fraction, and the `gauge` function provides the corresponding gauge reading.

## How to Run the Tests

1. Open your terminal.
2. Navigate to the directory where you have saved both `fuel.py` and `test_fuel.py`.

   ```
   cd path/to/your/directory
   ```

3. Run the tests using the `pytest` command:

   ```
   pytest test_fuel.py
   ```

4. The tests will be executed, and the results will be displayed in the terminal.

## Program Code

### fuel.py

```python
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
```

### test_fuel.py

```python
from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    with pytest.raises(ZeroDivisionError):
        convert('100/0')
    with pytest.raises(ValueError):
        convert('a/b')
    with pytest.raises(ValueError):
        convert('5/2')


def test_guage():
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
```

## How to Test

1. Run the tests as mentioned in the "How to Run the Tests" section.
2. The tests will be executed, and you will see the results in the terminal.

## Sample Test Cases

1. **Conversion Test ("1/4"):**
   - **Input:**
     ```
     assert convert("1/4") == 25
     ```

2. **Gauge Reading Test (25%):**
   - **Input:**
     ```
     assert gauge(25) == "25%"
     ```
     ```
     assert gauge(100) == "F"
     ```
     ```
     assert gauge(0) == "E"
     ```

3. **Zero Division Error Test:**
   - **Input:**
     ```
     with pytest.raises(ZeroDivisionError):
         convert('100/0')
     ```

4. **Value Error Test (Non-Digit Input):**
   - **Input:**
     ```
     with pytest.raises(ValueError):
         convert('a/b')
     ```

5. **Value Error Test (X > Y):**
   - **Input:**
     ```
     with pytest.raises(ValueError):
         convert('5/2')
     ```

## Additional Notes

- Ensure that the `fuel.py` and `test_fuel.py` files are saved in the same directory and have the correct names.
- The tests in `test_fuel.py` cover various scenarios to validate the correctness of the `convert` and `gauge` functions. Running the tests using `pytest` will indicate whether your implementation of these functions is working correctly.