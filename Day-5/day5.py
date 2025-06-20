from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up ChromeDriver
service = Service("D:/tools/chromedriver.exe")  # Change path if needed
driver = webdriver.Chrome(service=service)

# Step 1: Open Wikipedia
driver.get("https://www.wikipedia.org")

# Step 2: Wait for search input box and type
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchInput"))
)
search_box.clear()
search_box.send_keys("Bangladesh")

# Step 3: Wait for the search button and click it
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
search_button.click()

# Step 4: Wait for the new page to load and title to contain the keyword
WebDriverWait(driver, 10).until(
    EC.title_contains("Bangladesh")
)

# Step 5: Print the title
print("Page title:", driver.title)

# Optional: Wait and close
time.sleep(3)
driver.quit()
