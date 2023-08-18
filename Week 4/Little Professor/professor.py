import random


def main():
    n = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        problem = f"{x} + {y} = "
        answer = ""
        for _ in range(3):
            answer = input(problem)
            try:
                if int(answer) == x + y:
                    score += 1
                    break
                print("EEE")
            except ValueError:
                pass
        else:
            print(f"{x} + {y} = {x + y}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                continue
            return n
        except ValueError:
            pass


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError()
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10 ** (level - 1), 10 ** level - 1)


if __name__ == "__main__":
    main()