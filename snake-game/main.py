from turtle import Turtle,Screen
import time

is_game_on = True
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []
for position in starting_positions:
    snake_segment = Turtle(shape='square')
    snake_segment.penup()
    snake_segment.color('white')
    snake_segment.goto(position)
    segments.append(snake_segment)

while is_game_on:
    screen.update()
    time.sleep(0.1)
    # Second to the last Segment Code
    for seg_num in range(len(segments)-1,0,-1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)     

    segments[0].forward(20)  
    segments[0].left(90)   
# "Please commmit"
screen.exitonclick()
