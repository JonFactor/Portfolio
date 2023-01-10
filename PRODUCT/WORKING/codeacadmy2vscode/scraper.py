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
link = ''
with open('python\codeacadmy2vscode\local.txt', 'r') as loc:
    link = loc.read()
print(link)
############## running #################
try:
    driver.get(link)
    time.sleep(10)
finally:
    print('done')
    driver.quit()
############# Stopped ############
