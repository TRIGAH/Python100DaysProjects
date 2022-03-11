#THE LOVE CALCULATOR
print("Welcome to the Love Calculator!")

#Input Names
name1 = input("What is your name? \n")
name2 = input("What is your name? \n")

#Join Names
dating = (name1 + name2).lower()

true = 0
love = 0
score = ""

#True Counts
t = dating.count("t")
print(f"T occurs {t} times")
r = dating.count("r")
print(f"R occurs {r} times")
u = dating.count("u")
print(f"U occurs {u} times")
e = dating.count("e")
print(f"E occurs {e} times")
true = t + r + u + e 

#Blank Sapace
print("\n")

#Love Counts
l = dating.count("l")
print(f"L occurs {l} times")
o = dating.count("o")
print(f"O occurs {o} times")
v = dating.count("v")
print(f"V occurs {v} times")
e = dating.count("e")
print(f"E occurs {e} times")
love = l + o + v + e   

#Print Total of True and Love
print(f"Total = {true}")
print(f"Total = {love}")

#Joining True and Love
love_score = str(true) + str(love)

#Change Love Score to Integer
love_score_as_int = int(love_score)

if love_score_as_int < 10 or love_score_as_int > 90:
    print(f"Your Love Score is {love_score_as_int}, you go together like coke and mentos.")

elif love_score_as_int >= 40 and love_score_as_int <= 50:
    print(f"Your Love Score is {love_score_as_int}, you are alright together.")

else:
    print(f"Your Love Score is {love_score_as_int}")    


    