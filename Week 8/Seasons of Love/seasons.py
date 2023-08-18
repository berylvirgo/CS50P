import sys
from datetime import date, datetime
import re
import inflect


def main():
    dob = input("Date of Birth: ")
    print(convert_to_words(dob))


def convert_to_words(dob):
    p = inflect.engine()
    today = date.today()
    dob = get_dob(dob)
    dob = datetime.strptime(dob, "%Y-%m-%d").date()
    diff = today - dob
    minutes = diff.days * 24 * 60

    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"


def get_dob(dob):
    if match := re.match(r"^(\d{4}-\d{2}-\d{2})$", dob):
        return match.group(1)
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()