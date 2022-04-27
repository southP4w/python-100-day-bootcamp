# Write a program that simulates a coffee machine.

supplies = {
    "water": 10_000,
    "beans": 1_000,
    "tea-leaves": 1_000,
    "milk": 750,
    "sugar": 500
}

MENU = {
    "1": {  # coffee
        "ingredients": {
            "water": 10,
            "beans": 10
        },
        "price": 1.00
    },
    "2": {  # tea
        "ingredients": {
            "water": 12,
            "tea-leaves": 9
        },
        "price": .75
    }
}


def enough_supplies(ingredients):
    for item in ingredients:
        if supplies[item] < ingredients[item]:
            print(f"Sorry, we're out of {item}!")
            return False
    return True


def calculate_payment():
    print("Please insert your coins.")
    total = int(input("How many quarters? ")) * .25
    total += int(input("Dimes? ")) * .10
    total += int(input("Nickels? ")) * .05
    total += int(input("Pennies? ")) * .01
    return total


def enough_money(drink_price, user_payment):
    if drink_price < user_payment:
        change = round(user_payment - drink_price, 2)
        print(f"Here is your ${change} change. Enjoy!")
        return True
    elif drink_price > user_payment:
        print(f"${user_payment} is not enough!")
        return False
    print("Enjoy!")
    return True


def make_drink(drink, ingredients):
    for item in ingredients:
        supplies[item] -= drink[item]
    print(f"Enjoy your {drink}!")


turned_on = True
while turned_on:
    your_selection = input("What would you like to drink?\n\t1. Coffee\n\t2. Tea")
    if your_selection != "1" and your_selection != "2":
        print("Please make a valid selection")
    else:
        your_drink = MENU[your_selection]
        if enough_supplies(your_drink["ingredients"]):
            your_payment = calculate_payment()
            if enough_money(your_drink["price"], your_payment):
                make_drink(your_drink["ingredients"], your_selection)
