def main():
    if is_valid(input("Plate: ")):
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
    # Check if the string has no numbers in the middle
    if any(c.isdigit() for c in s[2:-2]) or s[-2] == "0":
        return False
    return True


def has_no_punctuation(s):
    # Check if the string contains no punctuation marks
    if all(c.isalpha() or c.isdigit() for c in s):
        return True
    return False


if __name__ == "__main__":
    main()