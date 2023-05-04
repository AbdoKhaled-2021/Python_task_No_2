def is_leap_year(year):
    """
    This function takes a year as input and returns True if it is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


if __name__ == "__main__":
    main()
