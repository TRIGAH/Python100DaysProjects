from turtle import Turtle,Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
maps_bet = screen.textinput(title='Make your bet', prompt='Which Turtle will win this race? Enter a Color: ')
turtle_colors = ['red','orange','yellow','green','blue','purple']
y_levels = [-100,-70,-40,-10,20,50]
all_turtles=[]
for idx,color in enumerate(turtle_colors):
    maps_turtle = Turtle(shape='turtle')
    maps_turtle.color(color)
    maps_turtle.penup()
    maps_turtle.goto(x=-230,y=y_levels[idx])
    all_turtles.append(maps_turtle)

if maps_bet:
    is_race_on = True    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == maps_bet:
                print(f"You've won...The winner is the {wining_color} turtle. ")
            else:
                print(f"You've lost...The winner is the {wining_color} turtle. ")
      
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()








































# def move_forward():
#     maps_turtle.forward(10)

# def move_back():
#     maps_turtle.backward(10)

# def move_clockwise():
#     maps_turtle.right(10)

# def move_counter_clockwise():
#     maps_turtle.left(10)

# def clear_screen():
#     maps_turtle.clear()
#     maps_turtle.penup()
#     maps_turtle.home()
#     maps_turtle.pendown()

# maps_turtle = Turtle()
# screen = Screen()
# screen.listen()
# screen.onkey(key="w",fun=move_forward)
# screen.onkey(key="s",fun=move_back)
# screen.onkey(key="a",fun=move_counter_clockwise)
# screen.onkey(key="d",fun=move_clockwise)
# screen.onkey(key="c",fun=clear_screen)  
# screen.exitonclick()