import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regular expression pattern to match the valid time formats
    pattern = r'^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$'
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid input format.")

    # Extracting hours and minutes from the input
    start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem = match.groups()

    # Set default values for minutes if not provided
    start_minute = start_minute or '00'
    end_minute = end_minute or '00'

    # Converting hours to integers
    start_hour = int(start_hour)
    end_hour = int(end_hour)
    start_minute = int(start_minute)
    end_minute = int(end_minute)

    # Handling invalid start and end times greater than 12
    if start_hour > 12 or end_hour > 12:
        raise ValueError("Invalid time. Hours should be between 1 and 12.")

    # Handling invalid minutes (should be between 0 and 59)
    if not (0 <= start_minute < 60) or not (0 <= end_minute < 60):
        raise ValueError("Invalid time. Minutes should be between 0 and 59.")

    # Handling 12-hour to 24-hour conversion
    if start_meridiem == "PM" and start_hour != 12:
        start_hour += 12
    elif start_meridiem == "AM" and start_hour == 12:
        start_hour = 0
    if end_meridiem == "PM" and end_hour != 12:
        end_hour += 12
    elif end_meridiem == "AM" and end_hour == 12:
        end_hour = 0

    # Formatting the output in 24-hour format
    start_time_24h = "{:02d}:{:02d}".format(start_hour, start_minute)
    end_time_24h = "{:02d}:{:02d}".format(end_hour, end_minute)
    return f"{start_time_24h} to {end_time_24h}"


if __name__ == "__main__":
    main()