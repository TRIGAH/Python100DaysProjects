from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('white')
        self.goto(0,250)
        with open ("..\score.txt", "r") as h_score:   
            self.high_score=h_score.read()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):  
        self.clear()  
        self.write(f"Score: {self.score},High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

        
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open ("..\score.txt", "w") as high_score:   
                high_score.write(f"{self.high_score}") 
        self.score = 0
        self.update_scoreboard()     

