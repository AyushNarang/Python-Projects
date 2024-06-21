from turtle import Turtle, Screen
from screen_setup import ScreenSetup
from user_paddle import UserPaddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen_set = ScreenSetup()
l_paddle = UserPaddle((-350, 0))
r_paddle = UserPaddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

flag = False
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect Collision with paddle
    if ball.xcor() > 320 or ball.xcor() < -320:
        if l_paddle.distance(ball) < 50 or r_paddle.distance(ball) < 50:
            ball.change_pad()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_wall()

    # Detect Right Miss
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_increase()
    # Detect Left Miss
    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_increase()


screen.exitonclick()