from turtle import Turtle
FONT = ('Arial', 32, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 240)
        self.write(arg=f"{self.l_score}", font=FONT)
        self.goto(200, 240)
        self.write(arg=f"{self.r_score}", font=FONT)

    def l_increase(self):
        self.l_score += 1
        self.update_score()

    def r_increase(self):
        self.r_score += 1
        self.update_score()
