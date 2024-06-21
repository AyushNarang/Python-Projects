from turtle import Turtle
MOVE = 20
UP = 90
DOWN = 270
STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)
        self.game_speed = 0.05

    def go_up(self):
        self.forward(MOVE)

    def go_down(self):
        self.backward(MOVE)

    def reset_player(self):
        self.goto(STARTING_POSITION)
        self.game_speed *= 0.5
