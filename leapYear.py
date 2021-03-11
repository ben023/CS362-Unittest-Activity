# Run with “python3 ben_lee_hw1.py”. 
# Enter a number when requested for user input, and it will print out whether it is a leap year or not.

def leapYear(year):
    if (year % 4 == 0 and year % 100 !=0):
        return("It is a leap year.")
    else:
        return("It is not a leap year.")

