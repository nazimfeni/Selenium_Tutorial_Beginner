# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# service =Service("D:/tools/chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# driver.get("https://www.google.com")
# time.sleep(5)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time

service = Service("D:/tools/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()