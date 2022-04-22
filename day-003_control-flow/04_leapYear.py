# Write a program that works out whether a given year is a leap year:
# On every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year
# is also evenly divisible by 400

is_leap_year = False
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
    else:
        is_leap_year = True

print(f"Leap year: {is_leap_year}")