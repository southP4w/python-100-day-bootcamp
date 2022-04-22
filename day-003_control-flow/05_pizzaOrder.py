# Write a program that calculates a customer's pizza order:
# 1. Small Pizza: $15
# 2. Medium Pizza: $20
# 3. Large Pizza: $25
# 4. Pepperoni for Small Pizza: +$2
# 5. Pepperoni for Medium or Large Pizza: +$3
# 6. Extra cheese for any size pizza: +$1

price = 0
size = input("Please choose your size (s, m, l): ").casefold()

while size != "s".casefold() and size != "sm".casefold() and size != "small".casefold() \
        and size != "m".casefold() and size != "med".casefold() and size != "medium".casefold() \
        and size != "l".casefold() and size != "lg".casefold() and size != "large".casefold():
    size = input("Please choose a valid option (sm, med, lg): ")

if size[0] == "s":
    price += 15
elif size[0] == "m":
    price += 20
elif size[0] == "l":
    price += 25
print(f"Total: ${price}")

pepperoni = input("Would you like pepperoni, you disgusting troglodyte? (Y/N): ")
while pepperoni != "y".casefold() and pepperoni != "yes".casefold() \
        and pepperoni != "n".casefold() and pepperoni != "no".casefold():
    pepperoni = input("Please choose a valid option (Y/N): ")

if pepperoni[0] == "y":
    if size[0] == "s":
        price += 2
    elif size[0] == "m" or size[0] == "l":
        price += 3
print(f"Total: ${price}")

extra_cheese = input("Would you like extra cheese, you disgusting troglodyte? (Y/N)")
while extra_cheese != "y".casefold() and extra_cheese != "yes".casefold() \
        and extra_cheese != "n".casefold() and extra_cheese != "no".casefold():
    extra_cheese = input("Please choose a valid option (Y/N): ")

if extra_cheese[0] == "y":
    price += 1
print(f"Total: ${price}")
