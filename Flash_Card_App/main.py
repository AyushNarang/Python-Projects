from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
french = ""
english = ""

try:
    data_frame = pandas.read_csv("./data/new_words.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("./data/french_words.csv")

data = data_frame.to_dict(orient="records")

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


# --------------------------------BUTTON LOGIC----------------------------------#
def right_ans():
    new_data = [i for i in data if i["French"] != french]
    new_frame = pandas.DataFrame(new_data)
    new_frame.to_csv("./data/new_words.csv", index=False)
    random_word()


def random_word():
    global french, english, flip_timer
    window.after_cancel(flip_timer)
    random_row = random.choice(data)
    french_word = random_row['French']
    english_word = random_row['English']
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, card_flip)
    french = french_word
    english = english_word


def card_flip():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=english)


# ----------------------------------UI SETUP-------------------------------------#
# White Box
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
back_img = PhotoImage(file="./images/card_back.png")

title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 25, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
flip_timer = window.after(3000, card_flip)

# ---------------------------------WORDS-------------------------------------#
# Right or Wrong Buttons
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right, command=right_ans, highlightthickness=0, bg=BACKGROUND_COLOR, border=0)
wrong_button = Button(image=wrong, command=random_word, highlightthickness=0, bg=BACKGROUND_COLOR, border=0)
right_button.grid(column=0, row=1)
wrong_button.grid(column=1, row=1)

random_word()


window.mainloop()
