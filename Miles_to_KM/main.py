from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Convert Function
def convert():
    miles = miles_entry.get()
    km = float(miles) * 1.609
    km_label.config(text=f"{round(km,2)}")

# Miles Entry
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 14, "normal"))
miles_label.grid(column=2, row=0)

# Equal Label
equal_label = Label(text="is equal to", font=("Arial", 14, "normal"))
equal_label.grid(column=0, row=1)

# KM Label
km_label = Label(text="0", font=("Arial", 14, "normal"))
km_label.grid(column=1, row=1)

# Km Text Label
km_text = Label(text="Km", font=("Arial", 14, "normal"))
km_text.grid(column=2, row=1)
km_text.config(padx=30, pady=30)

# Calc Button
cal_button = Button(text="Calculate", command=convert)
cal_button.grid(column=1, row=2)



window.mainloop()