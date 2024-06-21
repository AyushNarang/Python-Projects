from turtle import Turtle
FORWARD = 10
END = -300
ALIGN = "center"
FONT = ('Arial', 32, 'normal')


class ScreenSetup(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.draw_start()

    def draw_start(self):
        self.goto(0, 300)
        self.setheading(270)
        flag = True
        while flag:
            self.forward(FORWARD)
            self.penup()
            self.forward(FORWARD)
            self.pendown()
            if self.ycor() == END:
                flag = False

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
