from turtle import Turtle
MOVE = 40
END = 280


class UserPaddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor()+MOVE)

    def go_down(self):
        self.goto(self.xcor(), self.ycor()-MOVE)
