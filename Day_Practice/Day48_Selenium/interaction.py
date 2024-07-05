from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# article_count.click()
# founder_link = driver.find_element(By.LINK_TEXT, value="Founder")
# founder_link.click()

# Search for value
# driver.get("https://www.google.com/")
# search_bar = driver.find_element(By.ID, value="APjFqb")
# search_bar.send_keys("Python", Keys.ENTER)

# Filling a Form
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Jagjsini")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Iganwlkejn")
email = driver.find_element(By.NAME, value="email")
email.send_keys("agsidnaowgn@iogang.com")
submit = driver.find_element(By.XPATH, value="/html/body/form/button")
submit.click()

# driver.quit()