#Find out if the Year you are thinking of is a LEAP YEAR?
print("Welcome to the LEAP YEAR finder")

leap_year = float(input("Enter a Year ")) 

if leap_year % 4 == 0 and leap_year % 100 == 0 and leap_year % 400 == 0:
    print(f"{leap_year} is a Leap Year")
else:
    print("NOT A LEAP YEAR")    


