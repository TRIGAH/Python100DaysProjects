from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.starting_positions = [(0,0),(-20,0),(-40,0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self,position): 
        snake_segment = Turtle(shape='square')
        snake_segment.penup()
        snake_segment.color('white')
        snake_segment.goto(position)
        self.segments.append(snake_segment) 

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake() 
        self.head = self.segments[0]  

    def extend(self):
        self.add_segment(self.segments[-1].position())              

    def move(self): 
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)     

        self.head.forward(20) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
