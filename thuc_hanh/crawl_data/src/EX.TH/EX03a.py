from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Tạo tùy chọn
options = webdriver.firefox.options.Options()
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False

# Khởi tạo driver
driver = webdriver.Firefox(options = options)

# Tạo url
url = 'http://pythonscraping.com/pages/files/form.html'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 2 giây
time.sleep(2)

firstname_input = driver.find_element(By.XPATH, "//input[@name='firstname']")
lastname_input = driver.find_element(By.XPATH, "//input[@name='lastname']")

firstname_input.send_keys('Nhat Tung')
time.sleep(1)
lastname_input.send_keys("Le")

time.sleep(2)
buttton = driver.find_element(By.XPATH, "//input[@type='submit']")
buttton.click()
time.sleep(5)

driver.quit()