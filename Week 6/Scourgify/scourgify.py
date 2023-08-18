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
                    new_students = {}
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