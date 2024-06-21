from turtle import Turtle
FONT = ('Courier', 24, 'normal')
POSITION = (-280, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.curr_level = 1
        self.penup()
        self.hideturtle()
        self.write_level()

    def write_level(self):
        self.clear()
        self.goto(POSITION)
        self.write(arg=f"Level: {self.curr_level}", font=FONT)

    def round_win(self):
        self.curr_level += 1
        self.write_level()

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER.", align="center", font=FONT)
