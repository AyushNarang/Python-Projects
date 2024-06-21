from tkinter import *
from tkinter import messagebox
from generator import Generator
import pyperclip
import json
FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    generate = Generator()
    password = generate.password
    pass_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website_name = website_entry.get()
    username = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website_name: {
            "email": username,
            "password": password,
        }
    }

    if len(website_name)==0 or len(username)==0 or len(password)==0:
        messagebox.showerror(title="Error", message="One or more fields are empty!")
        return

    if messagebox.askyesno(title="Check Details", message=f"Are you sure these details are correct? "
                                                          f"\nUsername: {username} \nPassword: {password}\n"):
        try:
            with open("data.json", mode='r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode='w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)
            website_entry.focus()


# ------------------------------ SEARCH ------------------------------- #
def search_pass():
    website = website_entry.get().capitalize()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Oops", message="No details for the website exist.")
    else:
        new_data = {key: value for (key, value) in data.items() if website == key}
        messagebox.showinfo(title="Details",
                        message=f"The details are as follows: \nEmail: {new_data[website]['email']}\nPassword: {new_data[website]['password']}")

    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Text Labels
website_label = Label(text="Website:", font=(FONT_NAME, 9, "normal"))
email_label = Label(text="Email/Username:", font=(FONT_NAME, 9, "normal"))
password_label = Label(text="Password:", font=(FONT_NAME, 9, "normal"))
website_label.grid(column=0,row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1)

user_entry = Entry(width=50)
user_entry.insert(0, string="abc@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2)

pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_pass, width=14)
add_button = Button(text="Add", command=save_pass, width=36)
generate_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", command=search_pass, width=14)
search_button.grid(column=2, row=1)

window.mainloop()