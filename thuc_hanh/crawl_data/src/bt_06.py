from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

import pandas as pd
import re

service = Service(r'C:\Users\DELL\Documents\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)

all_links = []
for i in range(70, 71):
    url = f"https:\\en.wikipedia.org/wiki/list of painters by name beginning with %22{chr(i)}%22"
    try:
        driver.get(url)

        time.sleep(1)

        ul_tags = driver.find_elements(By.TAG_NAME, "ul")

        ul_painters = ul_tags[19]

        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]

        for link in links:
            all_links.append(link)
    except Exception as e:
        print(f"Error: {e}")

all_painter_data = []

count = 0
for link in all_links:
    if count > 3:
        break

    print(link)
    try:
        driver.get(link)
        time.sleep(1.5)
        try: 
            
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""

        try: 
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = birth_element.text
            birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
        except:
            birth = ""

        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = death_element.text
        except:
            death = ""

        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            nationality_element = nationality_element.find_element(By.CSS_SELECTOR, "div.birthplace")
            nationality = nationality_element.find_elements(By.TAG_NAME, 'a')[1].text
        except:
            nationality = ""
        
        all_painter_data.append([name, birth, death, nationality])
        count += 1
    except:
        pass

driver.quit()

columns = ['name', 'birth', 'death', 'nationality']
all_painter_df = pd.DataFrame(all_painter_data, columns=columns)

print(all_painter_df)

all_painter_df.to_csv('all_painter_data.csv', index=False)
print('Data Frame is written to csv file successfully.')