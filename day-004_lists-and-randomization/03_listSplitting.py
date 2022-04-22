# Write a program that takes a user's input and separates it into a list by a given character (a comma, in this case)
import random
names = input("Please list some names, each separated by a comma ','\n")
name_list = names.split(',')

print(name_list)

print(f"And the bill goes too... {name_list[random.randint(0, len(name_list) - 1)]}")
