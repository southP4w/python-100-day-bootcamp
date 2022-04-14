# Write a program for a roller-coaster ticket booth. The age and height requirements are as follows:
# 1. Height >= 120cm
# and
# 2. Age >= 8
# The price of tickets are as follows:
# 8-14 --> $11
# 14+  --> $15

print("Welcome to the Flag Sux Liability Lawsuit Machine!")
age = int(input("How many years old are you?\n"))

if age < 8:
    print("We'd let you ride because we need your money, but we've had too many lawsuits. You'll need to come back "
          "when you're 8 or older so that if you get killed, we're less likely to be liable because things.")
else:
    height = float(input("How many centimeters tall are you?\n"))
    if height < 120:
        print("You're too short.")
    else:
        if age < 14:
            price = 11
        else:
            price = 15
        print("Congratulations, you can ride the Liability Lawsuit Machine! Please board at your own risk. Flag Sux is "
              f"not responsible for your safety.\nYour price is: ${round(price)}.00")
