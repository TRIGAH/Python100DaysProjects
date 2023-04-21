from turtle import Turtle,Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

scoreboard = Scoreboard()

ball = Ball()


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

is_pong_on = True
while is_pong_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()   

    if ball.xcor() > 380:    
       ball.resetposition()
       scoreboard.l_point()
  
    if  ball.xcor() < -380:    
        ball.resetposition()
        scoreboard.r_point()
  
screen.exitonclick()