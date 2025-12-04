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

        ul_painters = ul_tags[19]

        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        titles = []
        for tag in li_tags:
            try:
                a = tag.find_element(By.TAG_NAME, "a")
                titles.append(a.get_attribute("title"))
            except:
                continue

        for title in titles:
            print(title)
    except Exception as e:
        print(f"Error: {e}")
    
driver.quit()