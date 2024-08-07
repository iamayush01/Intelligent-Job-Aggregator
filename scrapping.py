from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_job(company_details):
    driver = webdriver.Chrome()
    driver.get(company_details["url"])
    driver.implicitly_wait(50)
    jobs = driver.find_elements(By.CLASS_NAME, company_details["job_class_name"])
    job_list = []
    for job in jobs:
        try:
            title = job.find_element(By.CSS_SELECTOR, company_details["title_selector"]).text.strip()
            job_list.append({
                'title': title
            })
        except Exception as e:
            print(f"Error extracting title: {e}")
    driver.quit()
    return job_list