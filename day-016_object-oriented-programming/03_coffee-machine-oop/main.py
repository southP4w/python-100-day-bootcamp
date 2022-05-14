from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

money_machine.report()
coffee_maker.report()

turned_on = True
while turned_on:
    choices = menu.get_items()
    choice = input(f"\nWhat would you like to drink?\n{choices}\n")
    if choice not in choices:
        print("Please make a valid selection")
    else:
        your_drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(your_drink):
            if money_machine.make_payment(your_drink.cost):
                coffee_maker.make_coffee(your_drink)
                turned_on = False
                break
money_machine.report()
coffee_maker.report()
