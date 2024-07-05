from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:
    def __init__(self, down, up):
        # Keep Chrome browser open
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # Set up the driver for Chrome
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = down
        self.up = up

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, value=".start-text").click()
        time.sleep(60)
        self.up = float(self.driver.find_element(By.CSS_SELECTOR, value=".download-speed").text)
        self.down = float(self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed").text)
        self.driver.close()

    def tweet_at_provider(self, email, passw, prom_up, prom_down):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        username.click()
        username.send_keys(email, Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.click()
        password.send_keys(passw, Keys.ENTER)

        create_tweet = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        create_tweet.click()
        type_tweet = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
        type_tweet.click()
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {prom_down}down/{prom_up}up?"
        type_tweet.send_keys(tweet)
        time.sleep(1)
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')
        post_button.click()
