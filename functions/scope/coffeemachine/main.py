# Print Report
# Check resources sufficient
# Process Coins
# Check Transaction result
# Make coffee

MENU = {
    
    "espresso":{
    "ingredients":{
                    "water":50,
                    "coffee":18,
        },
        "cost":1.5,
    },

    "latte":{
    "ingredients":{
                    "water":200,
                    "milk":150,
                    "coffee":24,
        },
        "cost":2.5,
    },

    "cappuccino":{
    "ingredients":{
                    "water":250,
                    "milk":100,
                    "coffee":24,
        },
        "cost":3.0,
    },
}

resources = {
    "water":300,
    "milk":200,
    "coffee":100,
}


money = 0.00
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
is_on = True
status = False
def check_resources(coffee_type):
    """
    Returns True if resources is sufficient and False it its not
    """
    global water,milk,coffee
    global is_on,status
    if coffee_type != 'report':
        inkeys=list((MENU[str(coffee_type)]['ingredients']).keys())
        if 'water' in inkeys:
            cwater = MENU[str(coffee_type)]["ingredients"]["water"] 
            if water > cwater: 
                water-= cwater
                print(water)
            else:
                is_on=False
                print (f"Insufficient water to make {coffee_type}")     
        if 'coffee' in inkeys:
            ccoffee = MENU[str(coffee_type)]["ingredients"]["coffee"]  
            if coffee > ccoffee:
                coffee-= ccoffee
                print(coffee)
            else:
                is_on=False
                print (f"Insufficient coffee to make {coffee_type}")      
        if 'milk' in inkeys:
            cmilk = MENU[str(coffee_type)]["ingredients"]["milk"]  
            if milk > cmilk:
                milk-= cmilk
                print(milk)
            else:
                is_on=False
                print (f"Insufficient milk to make {coffee_type}")  
        status = True        
    elif coffee_type == 'report':
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}") 
    return status              

def perform_action(coffee_type):
    global status,is_on
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01
    if coffee_type == 'off'.lower():
        is_on = False
    if coffee_type == 'espresso'  or coffee_type == 'latte'  or coffee_type == 'cappuccino'  :
        print("Please insert coins. ")   
        quarter_amount = input("How many quarters?: ")
        quarter*= int(quarter_amount)
        dime_amount = input("How many dimes?: ")
        dime *= int(dime_amount)
        nickel_amount = input("How many nickles?: ")
        nickel *= int(nickel_amount)
        penny_amount = input("How many pennies?: ")
        penny *= int(penny_amount)
        money = quarter + dime + nickel + penny 
        status = check_resources(coffee_type)   
        if money < MENU[f"{coffee_type}"]["cost"]:       
            print("Insufficinet Funds. Money Refunded.")
        elif money >= MENU[f"{coffee_type}"]["cost"] and status == True:
            print(f"{coffee_type} served. Enjoy...👍")    

while is_on:
   coffee_type=input("What would you like? (espresso/latte/cappuccino): ")
   perform_action(coffee_type)




    # if coffee_type == 'espresso':
    #     cwater = MENU[str(coffee_type)]["ingredients"]["water"]  
    #     ccoffee = MENU[str(coffee_type)]["ingredients"]["coffee"]  
    #     if water > cwater and coffee > ccoffee:
    #         water -= cwater
    #         coffee -= ccoffee
    #     else:
    #         is_on = False
    #         print (f"No Sufficient Resources to make {coffee_type}")  
    #         return 
    # else: 
    #     cwater = MENU[str(coffee_type)]["ingredients"]["water"]  
    #     ccoffee = MENU[str(coffee_type)]["ingredients"]["coffee"]  
    #     cmilk = MENU[str(coffee_type)]["ingredients"]["milk"]     
    #     if water > cwater and coffee > ccoffee:
    #         water -= cwater
    #         coffee -= ccoffee
    #         milk -= cmilk
    #     else:
    #         is_on = False
    #         print (f"No Sufficient Resources to make {coffee_type}")  
    #         return
    #     return coffee_type 