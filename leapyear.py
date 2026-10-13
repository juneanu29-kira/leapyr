# Program to check whether a given year is a leap year or not
import sys
def leapyear(year):
    if (year %4 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


if __name__ == "__main__":
    year = int(sys.argv[1])
    leapyear(year)