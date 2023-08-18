def main():
    time = input("What time is it? ")
    converted_time = convert(time)

    if 7.00 <= converted_time <= 8.00:
        print("breakfast time")
    elif 12.00 <= converted_time <= 13.00:
        print("lunch time")
    elif 18.00 <= converted_time <= 19.00:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    time = float(hours) + float(minutes) / 60

    return time


if __name__ == "__main__":
    main()