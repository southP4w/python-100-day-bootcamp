# Write a program that simulates a coffee machine in an office.

supplies = {
    "water": 10_000,
    "beans": 1_000,
    "tea-leaves": 1_000,
    "milk": 750,
    "sugar": 500
}

MENU = {
    "coffee": {
        "ingredients": {
            "water": 10,
            "beans": 10
        },
        "cost": 1.00
    },
    "tea": {
        "ingredients": {
            "water": 12,
            "tea-leaves": 9
        },
        "cost": .75
    }
}


def enough_supplies(ingredients):
    for item in ingredients:
        if supplies[item] < ingredients[item]:
            print(f"Sorry, we're out of {item}!")
            return False


def calculate_payment():
    print("Please insert your coins.")
    total = int(input("How many quarters? ")) * .25
    total += int(input("Dimes? ")) * .10
    total += int(input("Nickels? ")) * .05
    total += int(input("Pennies? ")) * .01
    return total


turned_on = True
