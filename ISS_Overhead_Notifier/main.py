# Add your username and password for script to work.

import requests
import datetime
import smtplib
import time

# Change these according to yours
MY_LAT = 43.653225
MY_LONG = -79.383186


def check_for_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sunrise = int(sun_response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_response.json()["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.datetime.now().hour

    if sunrise > time_now > sunset:
        return True
    return False


def check_for_pos():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_lat = float(iss_response.json()["iss_position"]["latitude"])
    iss_lng = float(iss_response.json()["iss_position"]["longitude"])

    if MY_LAT+5 >= iss_lat >= MY_LAT-5 and MY_LONG+5 >= iss_lng >= MY_LONG-5:
        return True
    return False


# Add the details
username = ""
password = ""

while True:
    if check_for_pos():
        if check_for_dark():
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=username, password=password)
                connection.sendmail(from_addr=username,
                                    to_addrs=username,
                                    msg="Subject: LOOK UP!\n\nThe International Space Station is right above you!")
    time.sleep(60)
