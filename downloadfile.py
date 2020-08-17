import time 
from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    element1 = browser.find_element_by_xpath("//Input[@placeholder='Enter first name']")
    element1.send_keys("Kirill")
    element2 = browser.find_element_by_xpath("//Input[@placeholder='Enter last name']")
    element2.send_keys("Rostotskiy")
    element3 = browser.find_element_by_xpath("//Input[@placeholder='Enter email']")
    element3.send_keys("kamper1@yandex.ru")
    downloadFile = browser.find_element_by_id("file")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    downloadFile.send_keys(file_path)
    
    button = browser.find_element_by_css_selector(".btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()