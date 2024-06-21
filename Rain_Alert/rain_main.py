import smtplib
import os
import requests
api_key = os.environ.get("OWM_API_KEY")
my_email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
email_provider = "smtp.gmail.com"
message = "It will rain today, don't forget to bring an Umbrella!"

parameters = {"lat": 43.653225,
              "lon": -79.383186,
              "cnt": 4,
              "appid": api_key}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()['list']
will_rain = False
for i in weather_data:
    if i['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP(email_provider) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Rain Alert!\n\n {message}")
