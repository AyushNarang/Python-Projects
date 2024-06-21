from turtle import Turtle, Screen
import random

color_list = ["red", "green", "blue", "orange", "purple"]
turtle_list = []
start = -210
is_race_on = False

screen_1 = Screen()
screen_1.setup(width=500, height=400)
bet_win = screen_1.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")

for i in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[i])
    new_turtle.penup()
    start = start + 70
    new_turtle.goto(x=-230, y=start)
    turtle_list.append(new_turtle)

if bet_win:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            break

print(f"The winner was {winner}")
if bet_win == winner:
    print("Congratulations, you win.")
else:
    print("You lose.")

screen_1.exitonclick()