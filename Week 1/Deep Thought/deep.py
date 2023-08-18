def answer_to_life():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    answer = answer.strip().casefold()

    if answer in ("42", "forty-two", "forty two"):
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    print(answer_to_life())