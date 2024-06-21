import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

writing_obj = turtle.Turtle()
writing_obj.penup()
writing_obj.hideturtle()

# Get State's coordinates relative to map
# def get_mouse_click(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
correct_guess = 0
guess_list = []
while correct_guess != 50:
    answer_state = screen.textinput(title=f"{correct_guess}/50 States guessed", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    for state in data.state:
        if answer_state == state:
            correct_guess += 1
            guess_list.append(answer_state)
            correct_row = data[data.state == answer_state]
            writing_obj.goto(int(correct_row.x), int(correct_row.y))
            writing_obj.write(answer_state)

state_list = data.state.to_list()
miss_states = [i for i in state_list if i not in guess_list]

df = pandas.DataFrame(miss_states)
df.to_csv("Missed_States.csv")
