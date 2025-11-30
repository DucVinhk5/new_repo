from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

import pandas as pd
import re

service = Service(r'C:\Users\DELL\Documents\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)


url = "https://en.wikipedia.org/wiki/Edvard_Munch"
driver.get(url)

time.sleep(2)


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
    death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
except:
    death = ""

try:
    nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
    nationality = nationality_element.text
except:
    nationality = ""

driver.quit()

painter = {
    'name': name,
    'birth': birth,
    'death': death,
    'nationality': nationality
}

painter_df = pd.DataFrame([painter])

print(painter_df)