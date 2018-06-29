#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Firefox()

driver.get('http://www.cohpy.org')

print('The title is', driver.title)

element = driver.find_element_by_link_text("Brazenhead")
element.click()


WebDriverWait(driver, 20).until(
    lambda x: x.find_element_by_link_text(
        "hdrestaurants.com").is_displayed())
element = driver.find_element_by_link_text( "hdrestaurants.com")
element.click()
       







