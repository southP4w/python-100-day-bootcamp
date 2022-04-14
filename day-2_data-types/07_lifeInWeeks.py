# Write a program using maths and F-Strings that tells the user how many days, weeks, and/or months they have left if
# they were to live until 100 years old

age = float(input("What is your age?\n"))

years_remaining = 100 - age
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"Time left to live")
print(f"\tYears: {years_remaining}\n\tMonths: {months_remaining}\n\tWeeks: {weeks_remaining}\n\tDays: {days_remaining}")
