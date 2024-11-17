#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: "Jashanpreet Singh"
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month: int, year: int) -> int:
    """
    Returns the maximum number of days in a given month for a given year.
    Includes leap year calculations for February.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    return 0  # Default case (should not occur with valid input)

def after(date: str) -> str:
    """
    Given a date in YYYY-MM-DD format, return the next day's date.
    """
    # Split the input date string into year, month, and day
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    # Increment the day
    day += 1

    # If the day exceeds the max days in the month, reset day and increment month
    if day > mon_max(month, year):
        day = 1
        month += 1

        # If the month exceeds December, reset to January and increment the year
        if month > 12:
            month = 1
            year += 1

    # Format the date as YYYY-MM-DD and return
    return f"{year:04d}-{month:02d}-{day:02d}"

def usage():
    """
    Print a usage message to the user and exit.
    """
    message = "Usage: python3 assignment1.py <start_date> <stop_date>"
    print(message)  # Write to stdout
    sys.stderr.write(message + "\n")  # Also write to stderr
    sys.stdout.flush()
    sys.stderr.flush()
    sys.exit(1)  # Exit with a non-zero status


def leap_year(year: int) -> bool:
    """
    Returns True if the given year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

def valid_date(date: str) -> bool:
    """
    Check the validity of a date in YYYY-MM-DD format.
    Return True if valid, False otherwise.
    """
    try:
        # Split the date into components
        print(f"Checking date: {date}")  # Debugging statement
        parts = date.split('-')
        
        # Ensure the format is correct (YYYY-MM-DD)
        if len(parts) != 3:
            print("Invalid format: Must have three parts separated by '-'")
            return False

        str_year, str_month, str_day = parts
        if not (str_year.isdigit() and str_month.isdigit() and str_day.isdigit()):
            print("Invalid format: Year, month, and day must be numeric")
            return False

        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        # Ensure year is at least four digits
        if len(str_year) != 4:
            print(f"Invalid year format: {year}")
            return False

        # Check if the month is valid (1-12)
        if month < 1 or month > 12:
            print(f"Invalid month: {month}")
            return False

        # Check if the day is valid for the given month and year
        max_day = mon_max(month, year)
        print(f"Year: {year}, Month: {month}, Max Day: {max_day}, Day: {day}")  # Debugging statement
        if day < 1 or day > max_day:
            print(f"Invalid day: {day}")
            return False

        # If all checks pass, return True
        return True

    except (ValueError, TypeError) as e:
        # If there's an error during conversion or splitting, return False
        print(f"Error occurred with date: {date}, Error: {e}")
        return False

def day_count(start_date: str, stop_date: str) -> int:
    """
    Counts the number of weekend days (Saturday and Sunday) between two dates.
    Includes both start_date and stop_date.
    """
    count = 0
    current_date = start_date
    while current_date <= stop_date:
        day = day_of_week(*map(int, current_date.split('-')))  # Get the day of the week
        if day in ['sat', 'sun']:
            count += 1
        current_date = after(current_date)  # Move to the next date
    return count

if __name__ == "_main_":
    import sys

    # Debug message for argument count
    print(f"Debug: Number of arguments provided = {len(sys.argv)}", file=sys.stderr)

    # Check argument count
    if len(sys.argv) != 3:
        print("Debug: Incorrect number of arguments, calling usage()", file=sys.stderr)
        usage()  # Call usage() and exit
