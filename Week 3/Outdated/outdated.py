def main():
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ").strip()
        if "/" in date:
            splitted_date = date.split("/")
            if not splitted_date[0].isdigit():
                continue
            if int(splitted_date[0]) < 1 or int(splitted_date[0]) > 12:
                continue
            day = int(splitted_date[1])
            if day < 1 or day > 31:
                continue
            month = int(splitted_date[0])
            year = int(splitted_date[2])
            print(f"{year:04}-{month:02}-{day:02}")
            break
        elif " " in date:
            splitted_date = date.split(" ")
            if splitted_date[0] not in month_names:
                continue
            month = month_names.index(splitted_date[0]) + 1
            month = int(month)
            if not splitted_date[1].endswith(","):
                continue
            day = splitted_date[1].split(",")
            day = int(day[0])
            if month < 1 or month > 12:
                continue
            if day < 1 or day > 31:
                continue
            year = int(splitted_date[2])
            print(f"{year:04}-{month:02}-{day:02}")
            break
        else:
            continue
        if len(splitted_date) != 3:
            continue


if __name__ == "__main__":
    main()