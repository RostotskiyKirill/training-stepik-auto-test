import time 
from selenium import webdriver
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button = browser.find_element_by_css_selector (".btn")
    button.click()
    time.sleep(5)
    confirm = browser.switch_to.alert
    confirm.accept()
    
    def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
     
    x_element = browser.find_element_by_id("input_value").text
    x = x_element
    y = calc(x)
    
    field = browser.find_element_by_id ("answer")
    field.send_keys (y)
    
    button = browser.find_element_by_css_selector (".btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()