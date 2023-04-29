from turtle import Turtle
from paddle import Paddle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1,1)
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.x_move = 10
        self.y_move = 10
        self.y_random = random.randint(0,600)
        self.x_random = random.randint(0,800)
        self.move_speed = 0.1


    def move(self):
        new_y = self.ycor() +  self.y_move 
        new_x = self.xcor() +  self.x_move 
        self.goto(new_x,new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def resetposition(self):
        self.goto(0,0)
        self.x_bounce()   
        self.move_speed = 0.1 
