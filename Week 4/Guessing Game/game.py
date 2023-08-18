import random


def main():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1:
                continue
            level = random.randint(1, n)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess < 1:
                        continue
                    if guess < level:
                        print("Too small!")
                        continue
                    elif guess > level:
                        print("Too large!")
                        continue
                    else:
                        print("Just right!")
                        break
                except ValueError:
                    pass
            break
        except ValueError:
            pass


if __name__ == "__main__":
    main()