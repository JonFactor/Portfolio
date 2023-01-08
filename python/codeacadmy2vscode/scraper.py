############### imports ################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path 
import os 
import re 
import json
############### Defining ###############
PATH = "C:\Program Files (x86)\chromedriver.exe"# Home
#PATH = 'C:\\Users\Factor_Jon\Desktop\chromedriver.exe' #Skool
driver = webdriver.Chrome(PATH)
### get
grab = ''
with open('python\codeacadmy2vscode\local.txt', 'r') as loc:
    grab = loc.read()
############## running #################
try:
    driver.get(grab)
    time.sleep(1)
finally:
    print('done')
    driver.quit()
############# Stopped ############
