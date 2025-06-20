from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup ChromeDriver
service = Service("D:/tools/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")
time.sleep(2)

# Find the search box and enter text
search_box = driver.find_element(By.NAME, "q")
search_box.clear()  # Just in case it's not empty
search_box.send_keys("Selenium tutorial")  # Type in the box
time.sleep(1)

# Find the search button and click it
search_buttons = driver.find_elements(By.NAME, "btnK")

for btn in search_buttons:
    if btn.is_displayed():  # Make sure it's visible
        btn.click()
        break

# Wait for results to load
time.sleep(3)

# Print the title of the results page
print("Results page title:", driver.title)
# Close the browser
driver.quit()
