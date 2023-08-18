import sys
from PIL import Image, ImageOps


def main():
    images = []
    
    if len(sys.argv) == 3:
        if (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png") or sys.argv[1].endswith(".JPG") or sys.argv[1].endswith(".JPEG") or sys.argv[1].endswith(".PNG")) and (sys.argv[2].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[2].endswith(".png") or sys.argv[2].endswith(".JPG") or sys.argv[2].endswith(".JPEG") or sys.argv[2].endswith(".PNG")):
            if (sys.argv[1].endswith(".jpg") and sys.argv[2].endswith(".jpg")) or (sys.argv[1].endswith(".jpeg") and sys.argv[1].endswith(".jpeg")) or (sys.argv[1].endswith(".png") and sys.argv[2].endswith(".png")) or (sys.argv[1].endswith(".JPG") or sys.argv[2].endswith(".JPG")) or (sys.argv[1].endswith(".JPEG") or sys.argv[2].endswith(".JPEG")) or (sys.argv[1].endswith(".PNG") or sys.argv[2].endswith(".PNG")):
                try:
                    image = Image.open(sys.argv[1])
                except FileNotFoundError:
                    sys.exit(f"Could not read {sys.argv[1]}")
                shirt = Image.open("shirt.png")
                image = ImageOps.fit(image, shirt.size)
                image.paste(shirt, (0, 0), shirt)
                image.save(sys.argv[2])
            else:
                sys.exit("Input and Output have different extensions")
        else:
            sys.exit('Invalid input')
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()