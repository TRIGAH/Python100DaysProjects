from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0,9)

# def color_change(function):
#     def color_change_wrapper(guess):
#         return function(guess)
#     return color_change_wrapper

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1> <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="higher lower" width="300" height="300">'

@app.route('/<int:guess>')
def user_guess(guess):
    if guess < random_number:
        return '<h1 style="color:red;">Too Low</h1> <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="higher lower" width="300" height="300">'
    elif guess > random_number:
        return '<h1 style="color:purple;">Too High</h1> <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="higher lower" width="300" height="300">'
    else:
      return '<h1 style="color:green;">You Found Me</h1> <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="higher lower" width="300" height="300">'


print(random_number)

if __name__ == "__main__":
    app.run(debug=True)
