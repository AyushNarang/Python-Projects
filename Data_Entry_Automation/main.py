import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

static_website = "https://appbrewery.github.io/Zillow-Clone/"
FORM_LINK = ""

# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set up the driver for Chrome
driver = webdriver.Chrome(options=chrome_options)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
           "Accept-Language": "en-US,en;q=0.9"}

response = requests.get(static_website, headers=headers)
page = response.text

soup = BeautifulSoup(page, 'html.parser')

listings = soup.select(selector=".StyledPropertyCardDataWrapper a")
prices = soup.select(selector='.PropertyCardWrapper span')
addresses = soup.select(selector='.StyledPropertyCardDataWrapper address')
link_list = [listing.get('href') for listing in listings]
price_list = [price.text.split(' ')[0].strip('+/mo') for price in prices]
address_list = [address.text.replace("|", "").strip() for address in addresses]

driver.get(FORM_LINK)
time.sleep(3)
for i in range(0, len(link_list)):
    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_input.send_keys(address_list[i])
    price_input.send_keys(price_list[i])
    link_input.send_keys(link_list[i])
    driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    time.sleep(3)

driver.quit()
