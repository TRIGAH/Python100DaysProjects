from flask import Flask
from functools import wraps
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper  

def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper  

def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper  
 
def logging_decorator(function):
    def logging_wrapper(*args,**kwargs):
        print(function.__name__)
        print(args)
        return function("Maps")
    return logging_wrapper   

@app.route("/")
@make_bold
@make_underlined
@make_emphasis
def hello_world():
    return "Hello, World!"

@app.route("/<user>")
@logging_decorator
def hello_user(user):
    return f"<p>Hello, {user}!</p>"

if __name__ == "__main__":
    app.run(debug=True)