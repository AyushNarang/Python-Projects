from bs4 import BeautifulSoup
import requests
import smtplib

username = ""
password = ""

# url = input("Enter the item URL: ")
# max_price = input("Enter how much you are willing to pay for it: ")
# Temporary URL
url = "https://www.amazon.com/PHILIPS-Frameless-Replacement-Warranty-241V8LB/dp/B0C8ZKV5R9/ref=sr_1_3?dib=eyJ2IjoiMSJ9.nNa9UeGKY5mV6FJoFDtmSWf1Du8cFCkRv1KtaOl5lC4pc3I4cp90cL4OXaE6MDS3gYjlFpmDyuV4oxYuQGP5vvZnVdF3sWIkTaQha_IHLJbXBeUf5ZHoLthOUXhGXWpZUSLoKvN3zO1kZCTB1dm5lU4iNSrY-x8Pse-ls7de8VhG8br3MkCyJ20vOoKxinw8h7nKh1G9meQhhnSP0Sy8MR5fBqw61osJ8tLjOO2nE-R-0vYmxH1_zfoX6Et3Dz8HHCaxPHmXyXz8KygcrqkRc0o2nh3SlBEdHl-9op8p9_s.mBFpYSb9ewklCAhjPK4L6chmhKVdj0HrRW5ygL1ZUJs&dib_tag=se&keywords=24+inch+monitor&qid=1719950975&s=electronics&sr=1-3"
# Temporary Price
max_price = 90

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
           "Accept-Language": "en-US,en;q=0.9"}

response = requests.get(url=url, headers=headers)
page = response.text

soup = BeautifulSoup(page, 'html.parser')

price_tag = soup.find(name="span", class_="a-price-whole")
price = int(price_tag.getText().split('.')[0])

if price < max_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username,
                            to_addrs=username,
                            msg=f"Subject: Amazon Price Update Alert!\n\nThe Item you have been tracking on amazon "
                                f"with the link {url} has dropped in price to only {price}!\nHurry!")
