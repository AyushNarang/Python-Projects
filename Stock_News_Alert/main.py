import requests
import os
import datetime as dt
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')

parameters = {"function": "TIME_SERIES_DAILY",
              "symbol": STOCK,
              "outputsize": "compact",
              "apikey": STOCK_API_KEY}
stock_response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
current = float(stock_data_list[0]["4. close"])
prev = float(stock_data_list[1]["4. close"])

one_back = dt.datetime.now() - dt.timedelta(1)
news_parameters = {"qInTitle": "tesla",
                   "from": f"{one_back}",
                   "sortBy": "publishedAt",
                   "apiKey": f"{NEWS_API_KEY}"}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news_data = news_response.json()
change = round((((current - prev) / current) * 100), 2)
up_down = ""
if change > 0:
    up_down = "⬆"
else:
    up_down = "⬇"

news = news_data['articles']
three_articles = news[:3]
formatted_articles = [f"{STOCK}: {up_down}{change}% \nHeadline: {articles['title']}. \nBrief: {articles['description']}"
                      for articles in three_articles]

if abs(change) >= 0.1:
    for article in formatted_articles:
        message = f"{STOCK} Stock Update!\n\n{article}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                                msg=message)
