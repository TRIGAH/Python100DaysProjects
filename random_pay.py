import random

my_friends = input("Enter your Friends names seperated by a comma.")
print(my_friends)

name_split = my_friends.split(",")

pick = random.randint(0,len(name_split)-1)

print(f"{name_split[pick]} is to pay the bill")