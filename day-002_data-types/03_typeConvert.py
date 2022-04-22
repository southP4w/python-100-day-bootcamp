# Write a program that asks the user for their name and then tells them how many characters long their name is

num_char = len(input("What is your name?\n"))
num_char_string = str(num_char)     # convert num_char into a String
print("Your name is " + num_char_string + " characters long.")
