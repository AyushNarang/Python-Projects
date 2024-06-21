# Add your username and password for script to work.

import pandas
import datetime as dt
import random
import smtplib

data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
month = now.month
day = now.day

letter_num = random.randint(1, 3)
word = "[NAME]"
new_data = []

curr_row = data[(data['month'] == month) & (data['day'] == day)]
if curr_row.empty:
    print("none")
    pass
else:
    with open(f"./letter_templates/letter_{letter_num}.txt", "r") as letter:
        words = letter.readlines()
        for line in words:
            x = line.replace(word, curr_row['name'].item())
            new_data.append(x)

    message = "".join(new_data)
    # Put Email Address here
    my_email = ""
    password = ""
    # Change to correct email provider
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Make Connection Secure
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"{curr_row['email'].item()}",
                            msg=f"Subject:Testing Email\n\n {message}")



