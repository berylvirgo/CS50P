def main():
    text = input("")
    print(convert(text))


def convert(emoji):
    return emoji.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == "__main__":
    main()