from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Setup ChromeDriver
service = Service("D:/tools/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# List of websites to open
websites = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.wikipedia.org"
]

# Visit each website with a 2-second pause
for site in websites:
    driver.get(site)
    print(f"Opened: {site}")
    time.sleep(2)

# Close the browser
driver.quit()
