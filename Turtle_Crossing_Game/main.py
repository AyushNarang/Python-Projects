from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)

player = Player()
cars_list = []
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
run = 0

while game_is_on:
    screen.update()
    time.sleep(player.game_speed)
    run += 1
    if run == 6:
        car = Cars()
        cars_list.append(car)
        car.spawn_cars()
        run = 0
        for i in cars_list:
            i.forward(20)
            # Detect Collision with cars
            if player.distance(i) < 15:
                score.game_over()
                game_is_on = False

    # Detect when player reaches end
    if player.ycor() > 280:
        player.reset_player()
        score.round_win()

screen.exitonclick()