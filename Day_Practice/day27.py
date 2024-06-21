from tkinter import *


def button_clicked():
    print("Button Clicked")
    word = entry.get()
    my_label.config(text=word)
    # my_label.pack()


window = Tk()
window.title("First Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="This is the center", font=("Arial", 24, "bold"))
# my_label.place(x=100,y=0)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

entry = Entry(width=20)
# entry.pack()
entry.grid(column=3, row=2)
button_clicked()

# New Label
new_label = Label(text="New Text", font=("Arial", 24, "bold"))
new_label.grid(column=0, row=0)

# New Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

window.mainloop()