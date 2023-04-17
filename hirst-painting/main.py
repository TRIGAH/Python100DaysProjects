from turtle import Turtle,Screen,colormode
import random
color_list=[(202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212)]
colormode(255)
hirst_turtle=Turtle()
hirst_turtle.setheading(225)
hirst_turtle.penup()
hirst_turtle.forward(500)
hirst_turtle.setheading(360)
for dot_count in range(1,101):
    hirst_turtle.dot(15,random.choice(color_list))  
    hirst_turtle.forward(50)
    if dot_count % 10 == 0: 
        hirst_turtle.setheading(90)
        hirst_turtle.forward(50)
        hirst_turtle.setheading(180)
        hirst_turtle.forward(500)
        hirst_turtle.setheading(0)


screen = Screen()
screen.exitonclick()
