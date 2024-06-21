from turtle import Turtle, Screen

toto = Turtle()
toto.shape("turtle")
toto.speed("fastest")


def move_forward():
    toto.forward(10)

def move_back():
    toto.back(10)

def turn_clock():
    toto.setheading(toto.heading() - 10)

def turn_anticlock():
    toto.setheading(toto.heading() + 10)

def clear_screen():
    screen.reset()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=turn_clock)
screen.onkey(key="a", fun=turn_anticlock)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
