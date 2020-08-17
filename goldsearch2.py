import time 
from selenium import webdriver
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    sunduc = browser.find_element_by_id("treasure")
    sunduc_use = sunduc.get_attribute("valuex")

    def calc(x):
     return str(math.log(abs(12*math.sin(int(valuex)))))
     
    x_element = browser.find_element_by_id("input_value")
    x = x_element
    y = calc(x)
     
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    button = browser.find_element_by_css_selector(".btn")
    button.click()
  
finally:
    time.sleep(10)
    browser.quit()
  
  
  