import datetime as dt
import smtplib
from random import choice

now = dt.datetime.now()
day_of_week = now.weekday()

# Get the Message
with open("quotes.txt", "r") as file:
    message = file.readlines()
quote = str(choice(message))

# Put Email Address here
my_email = "narangayush23@gmail.com"
password = "czqj azfz miyi qozw"
# Change to correct email provider
with smtplib.SMTP("smtp.gmail.com") as connection:
    # Make Connection Secure
    connection.starttls()
    connection.login(user=my_email, password=password)
    # Set to monday for test
    day_of_week = 0
    if day_of_week == 0:
        connection.sendmail(from_addr=my_email,
                            to_addrs="narang23ayush@gmail.com",
                            msg=f"Subject:Happy Monday!\n\n{quote}")

