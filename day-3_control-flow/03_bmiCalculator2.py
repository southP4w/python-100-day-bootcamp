# Write a program that interprets a person's BMI based on weight and height:
# BMI < 18.5        --> underweight
# 18.5 <= BMI < 25  --> normal weight
# 25 < BMI < 30     --> slightly overweight
# 30 < BMI < 35     --> obese
# 35 < BMI          --> clinically obese

weight = float(input("What is your weight (in kilograms)?\n"))
height = float(input("What is your height (in meters^2)?\n"))

bmi = weight / height ** 2   # ** --> Exponent

print("Your BMI is", bmi, "kg")

if bmi < 18.5:
    print("You are underweight.")
elif bmi > 35:
    print("You are clinically obese.")
elif 18.5 <= bmi < 25:
    print("Your weight is normal.")
elif 25 < bmi < 30:
    print("You are slightly overweight.")
elif 30 < bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
