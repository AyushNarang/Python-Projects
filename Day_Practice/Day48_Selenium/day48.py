from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set up the driver for Chrome
driver = webdriver.Chrome(options=chrome_options)

# Amazon Price Track
# # Open the particular website
# driver.get("https://www.amazon.com/PHILIPS-Frameless-Replacement-Warranty-241V8LB/dp/B0C8ZKV5R9/ref=sr_1_3?dib=eyJ2IjoiMSJ9.nNa9UeGKY5mV6FJoFDtmSWf1Du8cFCkRv1KtaOl5lC4pc3I4cp90cL4OXaE6MDS3gYjlFpmDyuV4oxYuQGP5vvZnVdF3sWIkTaQha_IHLJbXBeUf5ZHoLthOUXhGXWpZUSLoKvN3zO1kZCTB1dm5lU4iNSrY-x8Pse-ls7de8VhG8br3MkCyJ20vOoKxinw8h7nKh1G9meQhhnSP0Sy8MR5fBqw61osJ8tLjOO2nE-R-0vYmxH1_zfoX6Et3Dz8HHCaxPHmXyXz8KygcrqkRc0o2nh3SlBEdHl-9op8p9_s.mBFpYSb9ewklCAhjPK4L6chmhKVdj0HrRW5ygL1ZUJs&dib_tag=se&keywords=24+inch+monitor&qid=1719950975&s=electronics&sr=1-3")
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# Python Search Bar
driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# submit_button = driver.find_element(By.ID, value="submit")
# print(submit_button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# # Using XPATH
# submit_bug = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_bug.text)

# Find the Upcoming Events
dates = driver.find_elements(By.CSS_SELECTOR, value='#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > a')
# for date in dates:
#     print(date.text)
# for name in event_names:
#     print(name.text)
list_of_events = {i: {'time': dates[i].text, 'name': event_names[i].text} for i in range(len(dates))}
print(list_of_events)

# driver.close()
driver.quit()