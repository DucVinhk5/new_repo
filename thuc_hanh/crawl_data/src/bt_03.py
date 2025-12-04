from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(r'C:\Users\DELL\Documents\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)

url = "https:\\en.wikipedia.org/wiki/list of painters by name beginning with %22P%22"
driver.get(url)

driver.maximize_window()

time.sleep(2)

ul_tags = driver.find_elements(By.TAG_NAME, "ul")

ul_painters = ul_tags[19]

li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

links = []
for tag in li_tags:
    try:
        a = tag.find_element(By.TAG_NAME, "a")
        links.append(a.get_attribute("href"))
    except:
        continue


titles = []
for tag in li_tags:
    try:
        a = tag.find_element(By.TAG_NAME, "a")
        titles.append(a.get_attribute("title"))
    except:
        continue


for link in links:
    print(link)

for title in titles:
    print(title)

driver.quit()