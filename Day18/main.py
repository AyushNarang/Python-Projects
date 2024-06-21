import turtle
from turtle import Turtle, Screen

toto = Turtle()
toto.shape("arrow")
turtle.colormode(255)

# for _ in range(4):
#     toto.forward(100)
#     toto.right(90)
# toto.home()

# for _ in range(10):
#     toto.forward(10)
#     toto.penup()
#     toto.forward(10)
#     toto.pendown()

# TODO: Different shapes
# angle = 0
#
# for i in range(3, 11):
#     angle = 360 / i
#     for j in range(0, i):
#         toto.forward(50)
#         toto.right(angle)

# TODO: Random Walk
import random as r
# colors = ["red", "blue", "orange", "purple", "black", "yellow"]


def random_color():
    red = r.randint(0,255)
    blue = r.randint(0, 255)
    green = r.randint(0, 255)
    color = (red, green, blue)
    return color


direction = [0, 90, 180, 270]
toto.speed(0)
toto.pensize(15)
def func():
    for _ in range(200):
        toto.color(random_color())
        toto.forward(25)
        toto.setheading(r.choice(direction))

# func()

# TODO: Spirograph


def spiro():
    toto.pensize(1)
    for _ in range(72):
        toto.color(random_color())
        toto.circle(100)
        toto.left(5)


def spiro_remove():
    for _ in range(72):
        toto.color("white")
        toto.circle(50)
        toto.setheading(toto.heading() + 5)

spiro()
spiro_remove()




my_screen = Screen()
my_screen.exitonclick()
