from turtle import Turtle
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('blue')
        self.goto(0,200)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):    
        self.write(f"Score= {self.score}", True, align=ALIGNMENT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", True, align=ALIGNMENT)
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()