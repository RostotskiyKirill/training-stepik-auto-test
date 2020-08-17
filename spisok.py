import time 
from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
 
    def calc():
     return str(int(x)+int(y))
     
    z = calc()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)

    button = browser.find_element_by_css_selector("button.btn").click()
    
finally:
    time.sleep(10)
    browser.quit()
    