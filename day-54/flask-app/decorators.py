import time


## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)


def speed_calc_decorator(function):
    def wrapper():
        current_time = time.time()
        function()
        end_time = time.time()
        finished_time = end_time - current_time
        print(finished_time)
    return wrapper     
    
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
















# import time
# def delay_timer(function):
#     def wrapper():
#         function("Maps")
#         function("Itohs")
#         function("Mayana")
#     return wrapper    

# @delay_timer
# def say_bye(name):
#     print (f"{name} bye")

# def say_hello():
#     print("hello")

# def say_greeting():
#     print("Good Morning")

# out = say_bye()
