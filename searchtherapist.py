import os
import time
from selenium import webdriver
# get the path of chromedriver
# dir = os.path.dirname(__file__)
chrome_driver_path = "C:\WebDrivers\chromedriver.exe"
#remove the .exe extension on linux or mac platform
# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(15)
driver.maximize_window()
# navigate to the application home page
driver.get("http://etherapyfinder.com/")
# Click search tab
search_therapist = driver.find_element_by_xpath('//a[@href="/therapist/search.php"]')
search_therapist.click()
time.sleep(5)

# Input some text into search field
search_field = driver.find_elements_by_id('search_form')
search_field.send_keys("Mary Christie")
#submit_btn = driver.find_element_by_id('button')
# search_field.clear()
#search_field[1].send_keys("Mary Christie")
#submit_btn.click()
# time.sleep(10)

