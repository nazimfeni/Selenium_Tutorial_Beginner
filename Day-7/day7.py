from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Setup ChromeDriver
service = Service("D:/tools/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open practice form
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(2)

# Accept cookies (if any)
try:
    driver.find_element(By.ID, "ez-accept-all").click()
    time.sleep(1)
except:
    pass

# Fill out the form
# 1. First name
driver.find_element(By.NAME, "firstname").send_keys("Nazim")

# 2. Last name
driver.find_element(By.NAME, "lastname").send_keys("Mamun")

# 3. Gender - Male
driver.find_element(By.ID, "sex-0").click()

# 4. Experience - 5 years
driver.find_element(By.ID, "exp-4").click()

# 5. Date
driver.find_element(By.ID, "datepicker").send_keys("06/20/2025")

# 6. Profession - Manual Tester
driver.find_element(By.ID, "profession-0").click()

# 7. Automation Tool - Selenium Webdriver
driver.find_element(By.ID, "tool-2").click()

# 8. Continent - Asia
continent = Select(driver.find_element(By.ID, "continents"))
continent.select_by_visible_text("Asia")

# 9. Selenium Command - Browser Commands
selenium_commands = Select(driver.find_element(By.ID, "selenium_commands"))
selenium_commands.select_by_visible_text("Browser Commands")

# 10. Submit
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

# Wait and close
time.sleep(3)
driver.quit()

