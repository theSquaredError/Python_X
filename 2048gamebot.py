from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,random


driver = webdriver.Chrome()

driver.get(' https://gabrielecirulli.github.io/2048/')

htmlElem = driver.find_element_by_tag_name('html')

#we will press the key in order up down right left
i=0
action = ['Keys.UP','Keys.DOWN','Keys.LEFT','Keys.RIGHT']
time.sleep(3)
for i in range(30):
	htmlElem.send_keys(Keys.UP)
	time.sleep(3)
	htmlElem.send_keys(Keys.DOWN)
	time.sleep(3)
	htmlElem.send_keys(Keys.LEFT)
	
