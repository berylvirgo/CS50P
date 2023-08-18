import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        match = matches(ip).split(".")
        return (0 <= int(match[0]) <= 255) and (0 <= int(match[1]) <= 255) and (0 <= int(match[2]) <= 255) and (0 <= int(match[3]) <= 255)
    except AttributeError:
        return False


def matches(ip):
    try:
        return re.search(r"^([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)$", ip).group(1)
    except AttributeError:
        return None


if __name__ == "__main__":
    main()