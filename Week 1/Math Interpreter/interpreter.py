def calculator():
    expression = input("Expression: ").split(" ")
    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])
    if y == "+":
        expression = x + z
    elif y == "-":
        expression = x - z
    elif y == "*":
        expression = x * z
    elif y == "/":
        expression = x / z
    return round(float(expression), 1)


if __name__ == "__main__":
    print(calculator())
