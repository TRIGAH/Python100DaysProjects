from art import logo
import random
import os
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
number = random.randint(1,100)
game_level = input("Choose Difficulty. Type 'easy' or 'hard': ") 
easy_attempts = 10
hard_attempts = 5
attempts = 0
is_gameover=False
def level():
    print(number)
    if game_level.lower() == 'easy':
        print(f"You have {easy_attempts} attempts remaining to guess the number.")
    elif game_level.lower() == 'hard':
        print(f"You have {hard_attempts} attempts remaining to guess the number.")  
level()
def compare(guess,number):
    if int(guess) > number:
        print("Too High")
        print("Guess Again")
    elif int(guess) < number: 
        print("Too Low")
        print("Guess Again")  

def guessing(guess):
    if game_level.lower() == 'easy' and guess != number:
        compare(guess,number)
        return f"You have {easy_attempts-attempts} attempts remaining to guess the number."
    elif game_level.lower() == 'hard' and guess != number:
        compare(guess,number)
        return f"You have {hard_attempts-attempts} attempts remaining to guess the number."

while not is_gameover:
    guess = input("Make a guess: ")
    attempts+=1
    print(guessing(guess))      
    if int(guess) == number:
        is_gameover =True
        print("You WIN")
        if input("Would you like to play again? 'y' or 'n': ") == 'y':
            level()
            is_gameover = False
            attempts=0
    elif game_level.lower() == 'easy' and attempts == easy_attempts:
        is_gameover =True
        print("Trials Exhuasted.. You Lose")  
    elif game_level.lower() == 'hard' and attempts == hard_attempts:
        is_gameover =True
        print("Trials Exhuasted.. You Lose")    


