from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
items = Menu()
cmaker = CoffeeMaker()
mmachine = MoneyMachine()
while is_on:
    choice =input(f"What would you like to drink {items.get_items()}: ")
    drink = items.find_drink(choice)
    if choice == 'off':
       is_on = False
    elif choice == 'report':
       cmaker.report()
       mmachine.report()
    else:
        status = cmaker.is_resource_sufficient(drink)
        if status == True:
            pay=mmachine.make_payment(float(drink.cost)) 
            if pay == True:
                cmaker.make_coffee(drink)
            else:
                is_on = False
        else:
            is_on = False           
 
