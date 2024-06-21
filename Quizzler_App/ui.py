from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="", width=280, font=(FONT, 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        # Buttons
        right_img = PhotoImage(file="./images/true.png")
        wrong_img = PhotoImage(file="./images/false.png")
        self.right_button = Button(image=right_img, border=0, highlightthickness=0, command=self.true_pressed)
        self.wrong_button = Button(image=wrong_img, border=0, highlightthickness=0, command=self.false_pressed)
        self.right_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)

        # Score Text
        self.score_label = Label(text=f"Score: {self.quiz.score}", font=(FONT, 12, "normal"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        response = self.quiz.check_answer("True")
        self.change_bg(response)

    def false_pressed(self):
        response = self.quiz.check_answer("False")
        self.change_bg(response)

    def change_bg(self, response):
        if response is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
