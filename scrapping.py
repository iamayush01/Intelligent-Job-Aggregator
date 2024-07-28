from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("")
driver.implicitly_wait(30)
jobs = driver.find_elements(By.CLASS_NAME, '')
for job in jobs:
    title = job.find_element(By.CLASS_NAME, '').text.strip()
    print(f"Title: {title}")
driver.quit()
