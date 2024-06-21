from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.update()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # scoreboard.game_over()
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect Collision with tail
    for i in snake.segment_list[1:]:
        if snake.head.distance(i) < 10:
            # scoreboard.game_over()
            scoreboard.reset_score()
            snake.reset_snake()
            # game_is_on = False


screen.exitonclick()
