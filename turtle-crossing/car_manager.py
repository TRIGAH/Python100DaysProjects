from turtle import Turtle
from player import Player
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ALIGNMENT = "center"

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.speed = 20

    def generate_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            y_new_car= random.randint(-250,250)
            new_car = Turtle()
            new_car.penup()
            new_car.goto(x=300,y=y_new_car)
            new_car.shape('square')
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(random.choice(COLORS)) 
            self.all_cars.append(new_car)  
    
    def move_cars(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.speed) 

    def increase_speed(self):
        self.speed += MOVE_INCREMENT




