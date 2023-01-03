############### imports ################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
############### Defining ###############

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
thelist = []
col = []
trnum = 0
rows = ''
num4rows = 100
tdnum = 1
############## running #################

try:
    driver.get('https://finviz.com/insidertrading.ashx')
    time.sleep(1)

    table_id = driver.find_element(By.XPATH, '/html/body/div[2]/div/table[2]')
    print('loaded')
    time.sleep(1)
    trnum +=2 
    while trnum <= num4rows:
        

        try:
            table_id.find_element(By.XPATH, f"/html/body/div[2]/div/table[2]/tbody/tr[{trnum}]/td[3]")
            print(trnum)
        except NoSuchElementException:
            trnum += 1
            pass
        
        

        
        rows = table_id.find_element(By.XPATH, f"/html/body/div[2]/div/table[2]/tbody/tr[{trnum}]")
        tdnum = 1
        while tdnum <= 10:
            try:
                rows.find_element(By.XPATH,f"/html/body/div[2]/div/table[2]/tbody/tr[{trnum}]/td[{tdnum}]")
            finally:
                col.append(rows.find_element(By.XPATH,f"/html/body/div[2]/div/table[2]/tbody/tr[{trnum}]/td[{tdnum}]").text) 
                tdnum += 1
        
        trnum+=1
finally:
    print('done')
    driver.quit()

    Tag = []
    Name = []
    Position = []
    Date = []
    Type = []
    Cost = []
    Cps = []
    a = 0
    while a < len(col):
        Tag.append(col[a])
        a +=10
    a = 1
    while a < len(col):
        Name.append(col[a])
        a += 10
    a = 2
    while a < len(col):
        Position.append(col[a])
        a += 10
    a = 3
    while a < len(col):
        Date.append(col[a])
        a += 10
    a = 4
    while a < len(col):
        Type.append(col[a])
        a += 10
    a = 5
    while a < len(col):
        Cps.append(col[a])
        a += 10
    a = 8
    while a < len(col):
        Cost.append(col[a])
        a += 10
    ID = 0
    Tags = {}
    Names = {}
    Positions = {}
    Types = {}
    Cpss = {}
    Costs = {}
    Dates = {}
    while ID < len(Tag):
        Tags.update(ID, Tag[ID])
        Names.update(ID, Name[ID])
        Positions.update(ID, Position[ID])
        Types.update(ID, Type[ID])
        Cpss.update(ID, Cps[ID])
        Costs.update(ID, Cost[ID])
        Dates.update(ID, Date[ID])
        ID +=1

    AllData = [
        Names,
        Positions,
        Types,
        Cpss,
        Costs,
        Dates
    ]
    
    print(AllData)