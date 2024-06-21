from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def change_pad(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def change_wall(self):
        self.y_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.change_pad()
