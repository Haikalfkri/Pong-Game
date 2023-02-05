from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        
        
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))
    
    def left_score(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def right_score(self):
        self.r_score += 1
        self.update_scoreboard()