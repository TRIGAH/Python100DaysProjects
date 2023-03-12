"""
-----GAME TEMPLATE-----

Logo(Fixed)
Comapare A: Shakira, a Musician, from Columbia.

vs logo
Against B: Shawn Mendes, a Musician, from Canada.
Who has more followers? Type 'A' or 'B':

if answer is right
clear previous option
You're right! Current Score: 1
(Repeat Above)
If answer is wrong
Sorry, that's wrong. Final Score: 2
end game
"""

from art import logo,vs
from game_data import data
import random
import os

is_gameover = False
current_score = 0
previous_choice = random.choice(data)
c_choice = random.choice(data)

# def format_data(acount):
#     return f"{acount['name']}, a {acount['description']}, from {acount['country']}."
# print(logo)
# print(f"Comapare A: {format_data(previous_choice)}")
# print(vs)
# print(f"Against B: {format_data(c_choice)}")

def game_choice():
    print(logo)
    global previous_choice
    current_choice = random.choice(data)
    A = previous_choice['follower_count']
    B = current_choice['follower_count']
    print(A)
    print(B)
    if previous_choice == current_choice:
        current_choice = random.choice(data)
    print(f"Comapare A: {previous_choice['name']}, a {previous_choice['description']}, from {previous_choice['country']}.")
    print(vs)
    print(f"Against B: {current_choice['name']}, a {current_choice['description']}, from {current_choice['country']}.")
    return current_choice

def check_answer(answer,previous_choice,current_choice):
    global current_score
    global is_gameover
    A = previous_choice['follower_count']
    B = current_choice['follower_count']
    if A > B and answer == 'a'.lower():
        current_score +=1
        print(f"You're right! Current Score: {current_score}")
    elif B > A and answer == 'b'.lower():
        current_score +=1
        print(f"You're right! Current Score: {current_score}")
    else:
        game_choice()
        print(f"Sorry, that's wrong. Final Score: {current_score}")    
        is_gameover=True

while not is_gameover:
    current_choice=game_choice()
    if previous_choice == current_choice:
        c_choice=game_choice()
        previous_choice = c_choice   
    answer=input("Who has more followers? Type 'A' or 'B': ")
    os.system('cls')       
    check_answer(answer,previous_choice,current_choice) 
    previous_choice = current_choice




































