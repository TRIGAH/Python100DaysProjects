from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.game_level()   

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)  
        self.level = 1   

    def game_level(self):
        self.level += 1
        self.penup()
        self.goto(-230,230)
        self.write(f"Level {self.level}", align="center", font=FONT)
