# -*- coding: utf-8 -*-
"""
Created on Sun May 11 00:52:22 2017

@author: Shiavngi Pandey
"""

from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/shivangi pandey/Anaconda3/chromedriver/chromedriver.exe')

driver.get('https://www.linkdin.com')

driver.minimize_window()

email = driver.find_element_by_xpath('//*[@id="login-email"]')
email.send_keys('shivangipandey9798@gmail.com')

time.sleep(3)

password = driver.find_element_by_xpath('//*[@id="login-password"]')
password.send_keys('*********')

time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="login-submit"]')
login.click()

time.sleep(5)

search_bar = driver.find_element_by_xpath('//*[@id="ember760"]/input').send_keys('android developer')

search_button = driver.find_element_by_xpath('//*[@id="nav-search-controls-wormhole"]/button').click()

time.sleep(5)

people_button = driver.find_element_by_xpath('//*[@id="ember3497"]/ul/li[1]/button').click()

time.sleep(5)

connect_button = driver.find_element_by_xpath("//*[@class='search-result__actions--primary button-secondary-medium m5']")

for x in connect_button:
    x.click()
    time.sleep(3)
    sendNow_button = driver.find_element_by_xpath("//*[@class='button-primary-large ml3']")
    sendNow_button.click()
    time.sleep(3)
driver.get(driver.current_url)