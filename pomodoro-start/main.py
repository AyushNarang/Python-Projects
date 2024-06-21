from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps == 8:
        countdown(long_break_secs)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_secs)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_seconds)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    mins_left = int(count / 60)
    secs_left = count % 60

    if secs_left < 10:
        secs_left = f"0{secs_left}"
    if mins_left < 10:
        mins_left = f"0{mins_left}"

    canvas.itemconfig(timer_text, text=f"{mins_left}:{secs_left}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✓"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Text at top
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 42, "normal"))
timer_label.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=3, row=2)

# Check label
check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "normal"))
check_label.grid(column=1, row=3)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()