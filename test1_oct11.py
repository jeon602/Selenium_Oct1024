from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome("C:\hy\Downloads\chromedriver-win64\chromedriver-win64")

driver.get('http://woolstonmanor.co.uk/golf/')

time.sleep(3)

element =driver.find_element(By.CLASS_NAME, '').text

print(element)

driver.quit()