#Invest
print("Welcome to Pristin Capital Limited where you INVEST and get massive returns.")

#Princicapal
principal = float(input("How much will you like to invest? "))

#Duration
duration = int(input("For how long? "))

#Rate
rate=1.5

#Interest
interest = (principal * rate * duration)/100

print("Your interest after {} months of investment is {}".format(duration,interest))

#Current Balance
current_balance = principal + interest
print("Your Account Balance is {:.2f}".format(current_balance))

print(".................WITHDRAW YOUR MONEY..........................\n")

#Withdrawal Transaction
amount = float(input("How much will you like to withdraw? "))

current_balance-=amount
print("Your Account Balance is {:.2f}".format(current_balance))


if amount <= interest:
    interest -= amount
    print(f"Your Principal is {principal}")
    print(f"Your Interest is {interest}")
    print(f"Your Current Balance now is {current_balance}")
elif amount >= interest:
    principal -= amount 
    print(f"Your Principal is {principal}")
    print(f"Your Interest is {interest}")
    print(f"Your Current Balance now is {current_balance}")
elif amount == principal:
    principal -= amount 
    print(f"Your Principal is {principal}")
    print(f"Your Interest is {interest}")
    print(f"Your Current Balance now is {current_balance}")
    print("Your Account is INACTIVE")
elif amount == current_balance:
    current_balance -= amount
    print(f"Your Principal is {principal}")
    print(f"Your Interest is {interest}")
    print(f"Your Current Balance now is {current_balance}")
    print("Your Account is CLOSED")
elif amount > current_balance:
    print("OGA YOU HAVE INSUFFICIENT FUNDS") 
else:
    print("INCORRECT DETAILS INPUTED")           
