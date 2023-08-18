# Little Professor

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 4 - Little Professor Problem Set](https://cs50.harvard.edu/python/2022/psets/4/professor/). The `professor.py` program simulates a math practice session similar to the "Little Professor" toy. It generates a series of addition problems with randomly generated numbers and prompts the user to solve them. The user has up to three attempts to answer each question correctly. The program then provides the user's score based on the number of correct answers.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `professor.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python professor.py
   ```

4. The program will prompt you to enter a level (1, 2, or 3). Choose a level to determine the range of numbers used in the math problems.

5. The program will then present you with 10 addition problems. Enter your answers for each problem.

6. The program will provide feedback on whether your answers are correct, incorrect, or not in the correct format.

7. After answering all 10 questions, the program will display your score.

## Program Code

```python
# professor.py

import random

def main():
    n = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        problem = f"{x} + {y} = "
        answer = ""
        for _ in range(3):
            answer = input(problem)
            try:
                if int(answer) == x + y:
                    score += 1
                    break
                print("EEE")
            except ValueError:
                pass
        else:
            print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                continue
            return n
        except ValueError:
            pass

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError()
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10 ** (level - 1), 10 ** level - 1)

if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter a valid level (1, 2, or 3) as prompted.
3. Answer each question in the format `X + Y =`, where `X` and `Y` are non-negative integers.
4. The program will provide feedback and your score at the end.

## Sample Test Cases

1. **Invalid Level Input:**
   - **Input:**
     ```
     -1
     ```

2. **Invalid Level (Out of Range):**
   - **Input:**
     ```
     4
     ```

3. **Correct Level:**
   - **Input (Level):**
     ```
     1
     ```
   - **Input (Answer - Question 1):**
     ```
     3 + 4 = 7
     ```
   - **Input (Answer Incorrectly - Question 2):**
     ```
     5 + 9 = cat
     ```
     ```
     EEE
     ```
   - **Input (Answer Incorrectly - Question 2, Attempt 2):**
     ```
     5 + 9 = 7
     ```
     ```
     EEE
     ```
   - **Input (Answer Incorrectly - Question 2, Attempt 3):**
     ```
     5 + 9 = 10
     ```
     ```
     EEE
     ```
     ```
     5 + 9 = 14
     ```
     Answer the remaining questions correctly
   - **After Question 10:**
     ```
     Score: 9
     ```

## Additional Notes

- Make sure to save the `professor.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.
- The program uses the `random` module to generate random numbers within the specified range for the addition problems. The user's answers are compared to the correct sum to determine if they are correct. The program handles invalid answers and provides feedback accordingly.