import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(scissors)
print("WELCOME TO THE ROCK PAPER SCISSORS GAME")

# RULES OF THE GAME

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock

elements =[rock,paper,scissors]

system_choice = random.choice(elements)

user_choice = input("What do you choose? Enter 0 for Rock 1 for Paper 2 for Scissors: ")

if system_choice == elements[int(user_choice)]:
    print(".......SYSTEM.......")
    print(system_choice)
    print(".......USER.......")
    print(elements[int(user_choice)])
    print("its a Tie")
elif system_choice==scissors and elements[int(user_choice)]==rock:
    print(".......SYSTEM.......")
    print(system_choice)
    print(".......USER.......")
    print(elements[int(user_choice)])
    print("You Win")    
elif system_choice==rock and elements[int(user_choice)]==paper: 
    print(".......SYSTEM.......")
    print(system_choice)
    print(".......USER.......")
    print(elements[int(user_choice)])
    print("You Win")   

elif system_choice==rock and elements[int(user_choice)]==paper:
    print(".......SYSTEM.......")
    print(system_choice)
    print(".......USER.......")
    print(elements[int(user_choice)])
    print("You Win")    
else:
    print(".......SYSTEM.......")
    print(system_choice)
    print(".......USER.......")
    print(elements[int(user_choice)])
    print("You Lose")    