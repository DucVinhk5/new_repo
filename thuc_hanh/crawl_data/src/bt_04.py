from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(r'C:\Users\DELL\Documents\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)

for i in range(65, 91):
    url = f"https:\\en.wikipedia.org/wiki/list of painters by name beginning with %22{chr(i)}%22"
    try:
        driver.get(url)

        time.sleep(2)

        ul_tags = driver.find_elements(By.TAG_NAME, "ul")
        print(len(ul_tags))

        ul_painters = ul_tags[20]

        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title") for tag in li_tags]

        for title in titles:
            print(title)
    except Exception as e:
        print(f"Error: {e}")
    
driver.quit()