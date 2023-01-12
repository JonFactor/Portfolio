############### imports ################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path 
import json, string, re, os, time
############### Defining ###############
#PATH = "C:\Program Files (x86)\chromedriver.exe"# Home
PATH = 'C:\\Users\Factor_Jon\Desktop\chromedriver.exe' #Skool
driver = webdriver.Chrome(PATH)
### get
Assingment = 'he'
with open('Backups\MANUAL-FAILSAFE\codeacadmy2vscode\local.json', 'r') as loc:
    data = json.load(loc)
    link = data['link']
    clientEmail = data['email']
    clientPass = data['pass']

############## running #################
try:
    driver.get(link)
    ### login
    loginbtn = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div/div/div[2]/button')
    loginbtn.click()

    googlebtn = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div/div/div[1]/div/div[2]/div/ul/li[2]/form/button')
    googlebtn.click()

    email = driver.find_element(By.XPATH, value='//*[@id="identifierId"]')
    email.send_keys(clientEmail)
    email.send_keys(Keys.RETURN)
    time.sleep(2)
    passs = driver.find_element(By.XPATH,value='//*[@id="password"]/div[1]/div/div[1]/input')
    passs.send_keys(clientPass)
    passs.send_keys(Keys.RETURN)

    ### get code
    time.sleep(8)    
    codebox = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/main/div[2]/div/div/div[2]/div/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[4]')
    lines = 100
    textss = []
    texts = []
    defs = []
    lines = codebox.find_elements(By.CLASS_NAME, value='view-line')
    i = 1
    for line in lines:
        span = line.find_element(By.TAG_NAME, value='span')
        spans = span.find_elements(By.TAG_NAME, value='span')
        w = 0
        while w < len(spans):
            #refined = spans[w].text.replace("', '", '').replace(', "', '').replace('", ', '').replace("''", '"')

            texts.append(spans[w].text)
            deff = {
                'text':texts,
                'line':i
            }    
            defs.append(deff)       
            w += 1
        i += 1
        #texts.append(textss)
    Assingment = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/main/div[2]/div/div/div[1]/div/div/div/div[2]/div/span').text.replace('&', '').replace(' ','-')

finally:
    time.sleep(1)
    driver.quit()
############# Stopped ############
workdir = Path.cwd() / 'Backups' / 'MANUAL-FAILSAFE' / 'codeacadmy2vscode' / 'Work'
if not os.path.exists(workdir):
    workdir.mkdir()



with open(f'Backups\MANUAL-FAILSAFE\codeacadmy2vscode\\Work\\{Assingment}.txt', 'w') as out:
    w = 0
    linee = []
    while w < len(defs):
        this = defs[w]
        if this['line'] == w:
            linee.append(texts)
        out.writelines(str(linee))
        out.writelines('\n')
        w += 1

    out.close()
print('done')