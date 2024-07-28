from selenium import webdriver
from selenium.webdriver.common.by import By
def scrapping(driver,url,job_class_name,title_selector):
    driver.get(url)
    driver.implicitly_wait(20)
    jobs = driver.find_elements(By.CLASS_NAME, job_class_name)
    for job in jobs:
        try:
            title = job.find_element(By.CSS_SELECTOR, title_selector).text.strip()
            print(f"Title: {title}")
        except Exception as e:
            print(f"Error extracting title: {e}")

def main():
    driver = webdriver.Chrome()
    try:
        # Microsoft
        url = "https://jobs.careers.microsoft.com/global/en/search?q=Engineering&p=Research%2C%20Applied%2C%20%26%20Data%20Sciences&p=Software%20Engineering&exp=Students%20and%20graduates&ws=Microsoft%20on-site%20only&el=Bachelors&l=en_us&pg=1&pgSz=20&o=Relevance&flt=true"
        job_class_name = "ms-List-cell"
        title_selector = 'h2.MZGzlrn8gfgSs8TZHhv2'
        scrapping(driver,url,job_class_name,title_selector)
    finally:
        driver.quit()
if __name__ == "__main__":
    main()