#Welcome Message
print("Welcome to the Tip Calculator")

#Input your Bill
bill = float(input("How much is your Bill? $"))

#Tip percentage
tip = float(input("What percentage Tip will you like to give? 10, 20, 30, 40, 50? "))

#How many people are involved
people = float(input("How many people are to pay the tip "))

#How much each person should take
tip_per_person = bill * (tip/100)
total_bill = bill + tip_per_person
total_bill_per_person = total_bill/people
#Result
print(f"Tip per person ${tip_per_person}")
print(f"The Total Bill is ${total_bill}")
print("{:.2f}".format(total_bill_per_person))
