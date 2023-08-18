def main():
    camelCase = input("camelCase: ")

    snake_case = convert_to_snake(camelCase)
    print(f"snake_case: {snake_case}")


def convert_to_snake(camel):
    snake_case = ""
    for i in camel:
        if i == i.upper():
            i = i.replace(i, f"_{i.lower()}")
        snake_case += i
    return snake_case


if __name__ == "__main__":
    main()