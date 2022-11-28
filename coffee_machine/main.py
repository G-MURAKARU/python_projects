import math
from dataBase import menu, resources
from dataBase import denominations as den

# NB: menu and resources are dictionaries

# TODO 1. create functionality to print the status report of the coffee machine
def sitRep(resources, profit):
    resources["money":profit]
    for resource in resources:
        print(resource, ":", resources[resource])


# TODO 2. create functionality for customers to enter their choices of coffee
def orderCoffee(resources, profit):
    order = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if order != "report":
        number = int(input("How many? "))

    if order == "off":
        return 0
    elif order == "report":
        sitRep(resources, profit)
        return
    elif order == "espresso":
        return ["espresso", number]
    elif order == "latte":
        return ["latte", number]
    elif order == "cappuccino":
        return ["cappuccino", number]
    else:
        print("Unfortunately, we don't have that.")
        orderCoffee()
        # TODO 7. since this function returns something, need to catch it in a variable and use it elsewhere <- done


# TODO 3. check if there are sufficient resources to fulfill customer's order BEFORE asking for money. if not, suggest something for which there are enough resources
def resourcesCheck(menu, resources, order):
    choice = order[0]
    amount = order[1]

    water = (menu[choice]["ingredients"]["water"]) * amount
    coffee = (menu[choice]["ingredients"]["coffee"]) * amount

    if choice == "espresso":
        milk = 0
    else:
        milk = (menu[choice]["ingredients"]["milk"]) * amount

    waterLeft = resources["water"]
    coffeeLeft = resources["coffee"]
    milkLeft = resources["milk"]

    if water <= waterLeft and coffee <= coffeeLeft and milk <= milkLeft:
        waterLeft -= water
        coffeeLeft -= coffee
        milkLeft -= milk
        print("success")
        print(waterLeft, coffeeLeft, milkLeft)
        # TODO 10. create function that updates the coffee machine's resources
        resources = resourceChange(resources, waterLeft, coffeeLeft, milkLeft)
        return True
    else:
        insufficient = []

        if water > waterLeft:
            possible = math.floor(waterLeft / (menu[choice]["ingredients"]["water"]))
            if possible > 0:
                print("There is enough water for only {}.".format(possible))
                return False
            else:
                insufficient.append("water")

        if coffee > coffeeLeft:
            possible = math.floor(coffeeLeft / (menu[choice]["ingredients"]["coffee"]))
            if possible > 0:
                print("There is enough coffee for only {}.".format(possible))
                return False
            else:
                insufficient.append("coffee")

        if milk > milkLeft:
            possible = math.floor(milkLeft / (menu[choice]["ingredients"]["milk"]))
            if possible > 0:
                print("There is enough milk for only {}.".format(possible))
                return False
            else:
                insufficient.append("milk")

        if len(insufficient) == 1:
            print("Sorry, there isn't enough {}.".format(insufficient[0]))
        elif len(insufficient) == 2:
            print(
                "Sorry, there isn't enough {} or {}.".format(
                    insufficient[0], insufficient[1]
                )
            )
        elif len(insufficient) == 3:
            print(
                "Sorry, there isn't enough {}, {} or {}.".format(
                    insufficient[0], insufficient[1], insufficient[2]
                )
            )

        print("Please order something else.")
        return False


# TODO 6. "make coffee", ensure available resources are diminished accordingly
def resourceChange(resources, waterLeft, coffeeLeft, milkLeft):
    """changes the number of resources available to make coffee in the machine after orders"""
    resources["water"] = waterLeft
    resources["coffee"] = coffeeLeft
    resources["milk"] = milkLeft

    return resources


# TODO 4. ask for customer to pay: penny ($0.01), dime ($0.10), nickel ($0.05), quarter($0.25)
def payDay(menu, order):
    choice = order[0]
    amount = order[1]
    cash = 0

    cost = (menu[choice]["cost"]) * amount

    # TODO 5. check if the transaction is successful i.e. has the customer given enough money
    while cash < cost:
        print("You are to pay ${}.".format(str(cost - cash)))
        coin = input(
            "In what denomination will you pay? (penny, dime, nickel, quarter) "
        )
        totalCoins = int(input("How many of them? "))
        cash += den[coin] * totalCoins

    if cash > cost:
        cash -= cost
        print("Here you go. Your balance is ${}.".format(cash))
    else:
        print("You have no outstanding balance.")

    return cost


# TODO 8. create a function that controls everything sequentially
def coffeeMachine():
    profit = 0
    running = True
    valid = False

    # TODO 9. make sure it loops until turned off
    while running:
        order = orderCoffee(resources, profit)

        if order == 0:
            running = False
        elif order != None:
            valid = resourcesCheck(menu, resources, order)

            if valid:
                profit = payDay(menu, order)
                print("Enjoy your coffee!! ☕️")


coffeeMachine()
