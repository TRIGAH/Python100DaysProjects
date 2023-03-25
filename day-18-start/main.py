from turtle import Turtle,Screen, colormode
import random

maps_turtle = Turtle()
colors=["red","green","blue"]
colormode(255)
maps_turtle.speed("fastest")
def random_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)

# def draw_shape(num_side):
#     angle = 360/num_side
#     for _ in range(num_side):
#         maps_turtle.color(random_color())
#         maps_turtle.fd(100)
#         maps_turtle.rt(angle)

# for num_side in range(3,11):        
#     draw_shape(num_side)

# directions = [0,90,180,270]
# maps_turtle.pensize(10)
# maps_turtle.speed("fastest")
# for _ in range(200):
#         maps_turtle.color(random_color())
#         maps_turtle.fd(50)
#         maps_turtle.setheading(random.choice(directions)) 


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        maps_turtle.color(random_color())
        maps_turtle.circle(100)
        current_heading = maps_turtle.heading()
        maps_turtle.setheading(current_heading + size_of_gap)
draw_spirograph(5)        

maps_screen = Screen()
maps_screen.exitonclick()








