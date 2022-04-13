# Write a program that calculate the user's BMI (Body-Mass Index)
# The formula for BMI is:
# BMI = (weight/height^2)

weight = float(input("What is your weight (in kilograms)?\n"))
height = float(input("What is your height (in meters^2)?\n"))

result = weight / height ** 2   # ** --> Exponent

print("Your BMI is", result, "kg")
