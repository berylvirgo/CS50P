# Nutrition Facts

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 2 - Nutrition Facts Problem Set](https://cs50.harvard.edu/python/2022/psets/2/nutrition/), named `nutrition.py`, allows users to input a fruit and outputs the number of calories in one portion of that fruit, based on information from the FDA's poster for fruits. The program handles input in a case-insensitive manner and matches the input fruit with its corresponding calories from the provided list.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `nutrition.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the Python interpreter:

   ```
   python nutrition.py
   ```

4. The program will prompt you to enter a fruit. After you enter the fruit, it will output the number of calories in one portion of that fruit based on the FDA's information.

## Program Code

```python
# nutrition.py

def main():
    fruits = [
        {"name": "Apple", "calories": 130},
        {"name": "Avocado", "calories": 50},
        {"name": "Banana", "calories": 110},
        {"name": "Cantaloupe", "calories": 50},
        {"name": "Grapefruit", "calories": 60},
        {"name": "Grapes", "calories": 90},
        {"name": "Honeydew Melon", "calories": 50},
        {"name": "Kiwifruit", "calories": 90},
        {"name": "Lemon", "calories": 15},
        {"name": "Lime", "calories": 20},
        {"name": "Nectarine", "calories": 60},
        {"name": "Orange", "calories": 80},
        {"name": "Peach", "calories": 60},
        {"name": "Pear", "calories": 100},
        {"name": "Pineapple", "calories": 50},
        {"name": "Plums", "calories": 70},
        {"name": "Strawberries", "calories": 50},
        {"name": "Sweet Cherries", "calories": 100},
        {"name": "Tangerine", "calories": 50},
        {"name": "Watermelon", "calories": 80},
    ]

    item = input("Item: ")

    for fruit in fruits:
        if item.capitalize() == fruit["name"] or item.title() == fruit["name"]:
            calories = fruit["calories"]
            print(f"Calories: {calories}")
            return

    # If the loop completes without finding a match
    print("Fruit not found in the list.")


if __name__ == "__main__":
    main()
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Follow the prompts to enter various fruit names. Make sure to vary the casing of your input (e.g., "apple," "Apple," "APPLE").
3. The program will output the number of calories in one portion of the entered fruit if it matches the list of fruits. If the entered fruit is not found in the list, the program will display nothing.

## Sample Test Cases

1. **Input:** Apple
   **Result:** Calories: 130

2. **Input:** Avocado
   **Result:** Calories: 50

3. **Input:** Sweet Cherries
   **Result:** Calories: 100

4. **Input:** Tomato
   **Result:**

## Additional Notes

Make sure to save the `nutrition.py` file in the same directory where you are running the program. If you encounter any issues with the program not being found or not running as expected, ensure you are in the correct directory and have saved the file with the correct name.