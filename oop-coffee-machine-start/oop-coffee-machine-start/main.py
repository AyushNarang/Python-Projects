from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def start():
    obj1 = Menu()
    # obj2 = MenuItem()
    obj3 = CoffeeMaker()
    obj4 = MoneyMachine()
    while(True):
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == 'report':
            obj3.report()
            obj4.report()
        elif choice == 'off':
            return
        else:
            drink = obj1.find_drink(choice)
            if drink:
                can_make = obj3.is_resource_sufficient(drink)
                if can_make:
                    transaction_success = obj4.make_payment(drink.cost)
                    if transaction_success:
                        obj3.make_coffee(drink)

start()