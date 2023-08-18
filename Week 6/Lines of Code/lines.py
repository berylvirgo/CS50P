import sys


def main():
    print(lines())


def lines():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith('.py'):
            try:
                with open(sys.argv[1]) as file:
                    counter = 0
                    for line in file:
                        if not (remove_comments(line) or remove_docstrings(line) or remove_whitespace(line)):
                            counter += 1
                    return counter
            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a Python file')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Too few command-line arguments')


def remove_comments(line):
    return (line.lstrip().startswith('#'))


def remove_docstrings(line):
    return line.lstrip().startswith("'''")


def remove_whitespace(line):
    return len(line.lstrip()) == 0


if __name__ == "__main__":
    main()