from selenium import webdriver
from selenium.webdriver.common.by import By
def scrape_job(url,job_class_name,title_selector):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(40)
    jobs = driver.find_elements(By.CLASS_NAME, job_class_name)
    list = []
    for job in jobs:
        try:
            title = job.find_element(By.CSS_SELECTOR, title_selector).text.strip()
            
            list.append({
                'title' : title
            })
        except Exception as e:
            print(f"Error extracting title: {e}")
    driver.quit()
    return list