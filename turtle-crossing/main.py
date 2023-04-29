import time
from turtle import Screen
from player import Player,FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.cross,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_car()
    cars.move_cars()
    
    if player.ycor() > FINISH_LINE_Y:
        player.resetposition()
        scoreboard.clear()
        scoreboard.game_level()
        cars.increase_speed()

    for car in cars.all_cars:
        if car.distance(player) < 20 :
            game_is_on = False
            scoreboard.game_over()

   

screen.exitonclick()