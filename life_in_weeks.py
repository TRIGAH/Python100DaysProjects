#Your Age
age = input("What is your age? ")

years_left = 90 - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

message = f"You have {days_left} days left , {weeks_left} weeks left and {months_left} left to reach 90 years in your LIFE"
print(message)