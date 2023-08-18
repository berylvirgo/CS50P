import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()   

    if (len(sys.argv)) != 1 and (len(sys.argv)) != 3:
        sys.exit("Invalid usage")

    if len(sys.argv) == 1:
        text = input("Input: ")
        font = random.choice(fonts)
        figlet.setFont(font=font)
        print(f"Output: {figlet.renderText(text)}")

    if len(sys.argv) == 3:
        if sys.argv[1] != "-f" and "--font" or sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(f"Output: {figlet.renderText(text)}")


if __name__ == "__main__":
    main()