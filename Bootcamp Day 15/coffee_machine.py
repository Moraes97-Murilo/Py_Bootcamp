#first machine
from machine_memory import menu,resources,limit
import time

def see_resources():
    print(resources)
    try:
        withdraw = float(input("Type the amout of money do you want to withdraw (type 0 for don't withdraw): "))
        if withdraw > 0 and withdraw <= resources["money"]:
            resources["money"] -= withdraw
        rep = True
        while rep:
            repo = input("Select a resource to refuel (water, milk, coffee, money, nothing): ").lower()
            delta = (limit[repo])-resources[repo]
            if repo in list(resources.keys()) and delta > 0:
                refuel = float(input(f"The machine needs {delta} of {repo}.. Type the amount to refuel: "))
                resources[repo] += refuel
            elif delta <= 0:
                print("Be careful, the machine will overflow! ")
            elif repo == "nothing":
                print(resources)
                print("We recommend that you leave all resources at maximum. Restarting! ")
                rep = False
            else:
                print("Something's wrong, restarting! ")
    except:
        print("Something's wrong, restarting! ")
def operational(ing,drink):
    for i in ing:
        alfa = resources[i]
        if alfa < menu[drink]["ingredients"][i]:
            return False
    return True
def update_resources(drink,ing_list):
    for i in ing_list:
        resources[i] -= menu[drink]["ingredients"][i]
    resources["money"] += menu[drink]["cost"]
def calculator(order):
    cost = float(menu[order]["cost"])
    pay = float(input(f"Your coffee costs ${cost} \nEnter your money, please..\n--> "))
    if pay > cost:
        time.sleep(1)
        print(f"You got in ${round(pay-cost,2)} change..")
        time.sleep(2)
        print("Here's your coffee, enjoy it! ")
    elif pay == cost:
        time.sleep(2)
        print("Here's your coffee, enjoy it! ")
    else: 
        while pay < cost:
            pay += float(input(f"Your coffee will need more ${round(cost-pay,2)} \nEnter more money, please..\n--> "))
        if pay > cost:
            time.sleep(1)
            print(f"You got in ${round(pay-cost,2)} change..")
            time.sleep(2)
            print("Here's your coffee, enjoy it! ")
        else:
            time.sleep(2)
            print("Here's your coffee, enjoy it! ")
def barista(order):
    if order == "espresso":
        ing = list(menu[order]["ingredients"].keys())
        veri = operational(ing,order)
        if veri:
            calculator(order)
            update_resources(order,ing)
        else:
            print("Sorry, the machine doesn't have resources enough for that coffee.\nTry again later!")
    elif order == "latte":
        ing = list(menu[order]["ingredients"].keys())
        veri = operational(ing,order)
        if veri:
            calculator(order)
            update_resources(order,ing)
        else:
            print("Sorry, the machine doesn't have resources enough for that coffee.\nTry again later!")
    else:
        ing = list(menu[order]["ingredients"].keys())
        veri = operational(ing,order)
        if veri:
            calculator(order)
            update_resources(order,ing)
        else:
            print("Sorry, the machine doesn't have resources enough for that coffee.\nTry again later!")

run = True
while run:
    recipe = input("\nWelcome..What coffee do you want me to prepare? \nespresso, latte or cappuccino\nType OFF to leave..\n--> ").lower()
    if recipe in list(menu.keys()):
        barista(recipe)
    elif recipe == "resources":
        passw = input("Type the password: ")
        if passw == resources["password"]:
            see_resources()
        else:
            print("Password's wrong, restarting! ")
    elif recipe == "off":
        print("\nThank you, see you next time :) ")
        run = False
    else:
        print("Your choice doesn't match the options..")