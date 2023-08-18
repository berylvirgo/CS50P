def main():
    text_to_shorten = input("Input: ")

    print(f"Output: {shorten_text(text_to_shorten)}")


def shorten_text(text):
    converted_text = ""
    text = text.strip()
    for alphabet in text:
        if alphabet in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            alphabet = alphabet.strip(alphabet)
        converted_text += alphabet

    return converted_text


if __name__ == "__main__":
    main()