
#Calculator Project

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2   

def divide(n1,n2):
    if not n1/n2 == ZeroDivisionError():
        return n1/n2     
    else:
        return ZeroDivisionError        

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
    }
    
def calculator():
        x1=float(input("Enter first number: "))

        for symbol in operations:
            print(symbol)
        should_continue = True
        while should_continue: 
            operational_symbol = input("Pick an operation from the line above: ")    
            x2=float(input("Enter Next number: "))
            calculation_function = operations[operational_symbol]
            answer = calculation_function(x1,x2)
            print(f"{x1} {operational_symbol} {x2} = {answer}")   

            if input(f"Enter y to coninue calculating with the result {answer} or n to start a new calculation: ")=="y":
                x1=answer
            else:    
                should_continue=False
                calculator()
            
calculator()