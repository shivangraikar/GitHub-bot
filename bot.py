# -*- coding: utf-8 -*-
"""
@author: Shivang
"""
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chromedriver_path = "/Users/shivangraikar/Desktop/chromedriver"  #insert chromedriver path
chrome_service = Service(chromedriver_path)
webdriver = webdriver.Chrome(service=chrome_service)
webdriver.get('https://buildertrend.net/')

# =============================================================================
# Login
# =============================================================================

username = webdriver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys("deniz.tuncay@dnd-homes.com")  #specify username
password = webdriver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("Deniz4141.")  #specify password

button_login = webdriver.find_element(By.XPATH, '//*[@id="reactLoginListDiv"]/div/div/div/div/div/div[3]/div/div/div/form/button')
button_login.click()

financial_button = webdriver.find_element(By.XPATH, '//*[@id="reactMainNavigation"]/div/div[1]/div/div[6]/button')
financial_button.click()

cost_inbox = webdriver.find_element(By.XPATH, '//*[@id="reactMainNavigation"]/div/div[1]/div/div[6]/div/div/div/ul/li[7]/span/div/div/a/div/div/div[2]/div')
cost_inbox.click()

upload_receipt = webdriver.find_element(By.XPATH, '//*[@id="reactReceiptsListDiv"]/div/div/div/section/div/div[1]/div/header/a/button/span')
upload_receipt.click()

browse_file = webdriver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_bodyTagControl"]/div[14]/div/div[2]/div/div[2]/div/div/div[2]/form/main/div/div/div/div/div/span/div[1]/span/div/p[2]/a')
browse_file.send_keys("C:\\Users\\YourName\\Desktop\\YourFile.txt")

# =============================================================================
# Navigate to your clickable buttons using each row information from the forms.csv
# =============================================================================
