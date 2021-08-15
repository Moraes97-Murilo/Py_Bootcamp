from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

working = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while working:
    options = menu.get_items()
    user_choice = input(f"What coffee would you like? ({options}).. ").lower()
    if user_choice == "off":
        working = False
    elif user_choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        coffee = menu.find_drink(user_choice)
        if coffee == None:
            continue
        elif coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)