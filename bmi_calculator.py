#Let user enter Weight
weight = input("Whats your weight? ")

#Let user enter Height
height = input("Whats your height? ")

bmi= int(weight)/float(height) ** 2

print("Your BMI is {}".format(bmi))