# Scourgify

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 6 - Scourgify Problem Set](https://cs50.harvard.edu/python/2022/psets/6/scourgify/). The `scourgify.py` program reads student data from an existing CSV file, splits the combined "name" column into "first" and "last" columns, and writes the cleaned data to a new CSV file.

## How to Run the Program

1. Open your terminal.
2. Navigate to the directory where you have saved the `scourgify.py` file.

   ```
   cd path/to/your/directory
   ```

3. Run the program using the `python` command and provide the filenames of the input and output CSV files as arguments:

   ```
   python scourgify.py input.csv output.csv
   ```

   Replace `input.csv` with the name of the existing CSV file to read data from and `output.csv` with the name of the new CSV file to write cleaned data to.

## Program Code

### scourgify.py

```python
import sys
import csv

def main():
    students = []
    
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        students.append(row)

                with open(sys.argv[2], "w") as file:
                    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for student in students:
                        last, first = student["name"].split(", ")
                        writer.writerow({"first": first, "last": last, "house": student["house"]})
            except FileNotFoundError:
                sys.exit(f'Could not read {sys.argv[1]}')
        else:
            sys.exit('Not a CSV file')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Too few command-line arguments')

if __name__ == "__main__":
    main()
```

## How to Test

1. Follow the steps mentioned in the "How to Run the Program" section to run the `scourgify.py` program.
2. Provide the name of an existing CSV file as the first argument and the name of a new CSV file as the second argument.
    - sample `input.csv`
        
        ```
        name,house
        "Abbott, Hannah",Hufflepuff
        "Bell, Katie",Gryffindor
        "Bones, Susan",Hufflepuff
        "Boot, Terry",Ravenclaw
        "Brown, Lavender",Gryffindor
        "Bulstrode, Millicent",Slytherin
        "Chang, Cho",Ravenclaw
        "Clearwater, Penelope",Ravenclaw
        "Crabbe, Vincent",Slytherin
        "Creevey, Colin",Gryffindor
        "Creevey, Dennis",Gryffindor
        "Diggory, Cedric",Hufflepuff
        "Edgecombe, Marietta",Ravenclaw
        "Finch-Fletchley, Justin",Hufflepuff
        "Finnigan, Seamus",Gryffindor
        "Goldstein, Anthony",Ravenclaw
        "Goyle, Gregory",Slytherin
        "Granger, Hermione",Gryffindor
        "Johnson, Angelina",Gryffindor
        "Jordan, Lee",Gryffindor
        "Longbottom, Neville",Gryffindor
        "Lovegood, Luna",Ravenclaw
        "Lupin, Remus",Gryffindor
        "Malfoy, Draco",Slytherin
        "Malfoy, Scorpius",Slytherin
        "Macmillan, Ernie",Hufflepuff
        "McGonagall, Minerva",Gryffindor
        "Midgen, Eloise",Gryffindor
        "McLaggen, Cormac",Gryffindor
        "Montague, Graham",Slytherin
        "Nott, Theodore",Slytherin
        "Parkinson, Pansy",Slytherin
        "Patil, Padma",Gryffindor
        "Patil, Parvati",Gryffindor
        "Potter, Harry",Gryffindor
        "Riddle, Tom",Slytherin
        "Robins, Demelza",Gryffindor
        "Scamander, Newt",Hufflepuff
        "Slughorn, Horace",Slytherin
        "Smith, Zacharias",Hufflepuff
        "Snape, Severus",Slytherin
        "Spinnet, Alicia",Gryffindor
        "Sprout, Pomona",Hufflepuff
        "Thomas, Dean",Gryffindor
        "Vane, Romilda",Gryffindor
        "Warren, Myrtle",Ravenclaw
        "Weasley, Fred",Gryffindor
        "Weasley, George",Gryffindor
        "Weasley, Ginny",Gryffindor
        "Weasley, Percy",Gryffindor
        "Weasley, Ron",Gryffindor
        "Wood, Oliver",Gryffindor
        "Zabini, Blaise",Slytherin
        ```
3. The program will read data from the input CSV file, split the combined "name" column into "first" and "last" columns, and write the cleaned data to the output CSV file.

## Additional Notes

- The `scourgify.py` program uses the `csv` module to read data from the input CSV file and write cleaned data to the output CSV file.
- It performs error handling to handle cases where the user provides incorrect command-line arguments or the specified files do not exist.
- After running the program, it will create a new CSV file with cleaned data, splitting the "name" column into "first" and "last" columns.