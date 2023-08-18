import emoji

def main():
    prompt = input("Input: ")
    print(f"Output: {emoji.emojize(prompt, language='alias')}")


if __name__ == "__main__":
    main()