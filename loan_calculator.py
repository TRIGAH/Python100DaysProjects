#Recieve a LOAN in 30 Minutes
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


#Withdrawal Transaction
amount = float(input("How much will you like to withdraw? "))

current_balance-=amount
print("Your Account Balance is {:.2f}".format(current_balance))
