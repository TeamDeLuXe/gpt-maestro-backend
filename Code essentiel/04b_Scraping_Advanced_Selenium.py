from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://example.com")
title = browser.find_element(By.TAG_NAME, 'h1').text
print(title)
browser.quit()