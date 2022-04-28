#Get LOAN in 30 Minutes

loan_amount = input("How much do you need? ")

duration = input("For how long? ")

rate = 5

print(f"We are giving you {loan_amount} at a rate of {rate}%, do you want to proceed? Y/N ")

interest = float(loan_amount)*float(duration)*float(rate)/100

repayment_amount = float(loan_amount) + interest

amount_repayed = 0

print("You will pay Installmentally")

while repayment_amount !=0:
    amount_repayed = input("PAY: ")
    repayment_amount-=int(amount_repayed)
    print(f"You have an outstanding of {repayment_amount} left.")
else:
    print("You are a Good Guy")    
 