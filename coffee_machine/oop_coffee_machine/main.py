from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
payDay = MoneyMachine()


def machineRun():
    running = True

    while running:
        order = input("What would you like to order? (espresso/latte/cappuccino) ")

        if order == "off":
            running = False
        elif order == "report":
            coffeeMaker.report()
            payDay.report()
        else:
            orderObject = menu.find_drink(order)

            orderPossible = coffeeMaker.is_resource_sufficient(orderObject)

            if orderPossible:
                orderCost = orderObject.cost
                receivedPay = False
                while not receivedPay:
                    receivedPay = payDay.make_payment(orderCost)
                coffeeMaker.make_coffee(orderObject)


machineRun()
