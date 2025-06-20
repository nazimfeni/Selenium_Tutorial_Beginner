from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup driver
service = Service("D:/tools/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Wait a bit to make sure page loads
time.sleep(2)

# 1️⃣ Get and print the page title
print("Page title:", driver.title)

# 2️⃣ Find the search input box by 'name'
search_box = driver.find_element(By.NAME, "q")
print("Search box found:", search_box.get_attribute("name"))

# 3️⃣ Find the search button (Google Search)
search_buttons = driver.find_elements(By.NAME, "btnK")

# Sometimes there are 2 search buttons -- we pick the first visible one
for btn in search_buttons:
    if btn.is_displayed():
        print("Search button text:", btn.get_attribute("value"))
        break

# Keep browser open for a few seconds
time.sleep(5)
driver.quit()

