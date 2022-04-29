import random
import hangman_words,hangman_art

lives =6
chosen_word = random.choice(hangman_words.word_list)
print(f"{hangman_art.logo}")
print(f"The word to save a soul is {chosen_word}")  
chosen_word_list=[]
chosen_word_count = len(chosen_word)
end_of_game = False

for position in range(chosen_word_count):
        chosen_word_list += "-"    

print(chosen_word_list)    

while end_of_game==False:
        guess = input("Guess a correct letter to save a soul: ").lower()
        for position in range(chosen_word_count):

                if guess == chosen_word[position]:
                        chosen_word_list[position] = guess
        if guess not in chosen_word:

                print(f"You guessed {guess} which is wrong, and you will lose a life.")
                lives-=1
                print(f"You have {lives} lives left")
                print(hangman_art.stages[lives])
        elif guess in chosen_word_list:
            print(f"You have guessed {guess} before")                    

        print(chosen_word_list)                 
      
        if "-" not in chosen_word_list:
                end_of_game=True
                print("You Win!")
        elif lives == 0:
                end_of_game=True
                print("You Lose!")        



# end_of_game = False
# while not  end_of_game :
#     guess = input("Guess a correct letter to save a soul: ").lower()
#     for word in chosen_word:

#         if word == guess:
            
#             word = guess  
#             chosen_word_list.append(word)   

#         elif word != guess:
#             word = "-"    
#             chosen_word_list.append(word)   

#     print(chosen_word_list)

#     if "-" not in chosen_word_list:
#         end_of_game = False
#         print("You win")
     

