from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# Tùy chọn cho Firefox
options = Options()

options.headless = True  # Cho hiện giao diện

# Khởi tạo driver Firefox
driver = webdriver.Firefox(options=options)

# Tạo url
url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"

# Truy cập
driver.get(url)

print("Before: ================================\n")
print(driver.page_source)

time.sleep(3)

print("\n\n\n\nAfter: ================================\n")
print(driver.page_source)

driver.quit()
