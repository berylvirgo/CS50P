import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Using a regular expression to find all occurrences of "um" as a word
    um_occurrences = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(um_occurrences)


if __name__ == "__main__":
    main()