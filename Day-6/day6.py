from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Set up ChromeDriver
service = Service("D:/tools/chromedriver.exe")  # Update if needed
driver = webdriver.Chrome(service=service)

# Open Wikipedia
driver.get("https://www.wikipedia.org")
print("Opened:", driver.title)
time.sleep(2)

# Go to Python.org
driver.get("https://www.python.org")
print("Opened:", driver.title)
time.sleep(2)

# Go to DuckDuckGo
driver.get("https://www.duckduckgo.com")
print("Opened:", driver.title)
time.sleep(2)

# Go back to Python.org
driver.back()
print("Back to:", driver.title)
time.sleep(2)

# Go back to Wikipedia
driver.back()
print("Back to:", driver.title)
time.sleep(2)

# Go forward to Python.org
driver.forward()
print("Forward to:", driver.title)
time.sleep(2)

# Refresh the page
driver.refresh()
print("Page refreshed:", driver.title)
time.sleep(2)

# Print current URL
print("Current URL:", driver.current_url)

# Get all cookies
cookies = driver.get_cookies()
print("\nCookies:")
for cookie in cookies:
    print(cookie)

# Close the browser
driver.quit()
