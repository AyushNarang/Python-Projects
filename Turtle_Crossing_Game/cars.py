from turtle import Turtle
import random
X = 280


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.colors = ["red", "blue", "yellow", "green", "orange", "purple"]
        self.color(random.choice(self.colors))

    def spawn_cars(self):
        self.goto(X, random.randint(-250, 250))
        self.setheading(180)
