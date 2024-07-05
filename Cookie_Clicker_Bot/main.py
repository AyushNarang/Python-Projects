import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://orteil.dashnet.org/cookieclicker/")
#
# time.sleep(4)
# language_select = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
# language_select.click()
# time.sleep(4)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find the cookie
cookie = driver.find_element(By.ID, value="cookie")
# Create a list of upgrade ids
upgrades = driver.find_elements(By.CSS_SELECTOR, value='#store div')
upgrade_ids = [upgrade.get_attribute("id") for upgrade in upgrades]

timeout = time.time() + 5

while True:
    cookie.click()

    # Check every 5 seconds
    if time.time() > timeout:
        prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # List of item prices
        for price in prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Dictionary of all the cookie upgrades with key as price and value as id
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = upgrade_ids[n]

        # Checking the number of cookies we have
        cookie_count_content = driver.find_element(By.ID, value='money').text
        if "," in cookie_count_content:
            cookie_count_content.replace(",", "")
        cookie_count = int(cookie_count_content)

        # Dictionary of all upgrades we can afford
        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Getting the most expensive upgrade we can afford
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element(By.ID, value=to_purchase_id).click()

        # Adjust timeout value to check after 5 more seconds
        timeout = time.time() + 5


    # if cookie_count > 15:
    #     upgrade1 = driver.find_elements(By.CSS_SELECTOR, value='//*[@id="product0"]')
    #     upgrade1.click()

