# import smtplib
#
# # Put Email Address here
# my_email = ""
# password = ""
# # Change to correct email provider
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Make Connection Secure
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="narang23ayush@gmail.com",
#                         msg="Subject:Testing Email\n\nHello testing")

import datetime as dt

now = dt.datetime.now()

year = now.year

print(year)