# -*- coding: utf-8 -*-
"""
@author: Shivang
"""
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
import pandas as pd
from selenium.webdriver.chrome.service import Service

chromedriver_path = "/Users/shivangraikar/Desktop/chromedriver"  #insert chromedriver path
sleep(2)
chrome_service = Service(chromedriver_path)
webdriver = webdriver.Chrome(service=chrome_service)
webdriver.get('https://github.com/login')
sleep(3)

webdriver.quit()
# =============================================================================
# Login
# =============================================================================
username = webdriver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[2]')
username.send_keys("")  #specify username
password = webdriver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[3]')
password.send_keys("")  #specify password
sleep(5)

button_login = webdriver.find_element_by_xpath('/html/body/div[3]/main/div/div[4]/form/input[14]')
button_login.click()
sleep(3)

# =============================================================================
# Navigate to your clickable buttons
# =============================================================================