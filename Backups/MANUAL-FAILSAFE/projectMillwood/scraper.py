import os
from pathlib import Path
import pathlib
### settings
## cheeky varibles
TowerDir = Path('C:/TOWER')
link = 'https://esp.chep.com/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html'
user = 'e'
passs = 'r'
## make dir
if not os.path.exists(TowerDir):
    TowerDir.mkdir()
    
## opening CSV
def opencsv():
    with open(f'{TowerDir}\\CSV.json', 'w') as twr:
        pass


opencsv()
### Webscraper
## imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import json, string, re, os, time
## varibles
PATH = "C:\Program Files (x86)\chromedriver.exe"# Home

driver = webdriver.Chrome(PATH)
try:
 driver.get(link)
 time.sleep(1)
 driver.find_element(By.XPATH, '//*[@id="USERNAME_FIELD-inner"]').send_keys(user)
 driver.find_element(By.XPATH, '//*[@id="PASSWORD_FIELD-inner"]').send_keys(passs)
 driver.find_element(By.XPATH, '//*[@id="LOGIN_LINK"]').click()

finally:
    time.sleep(100)
    driver.quit()