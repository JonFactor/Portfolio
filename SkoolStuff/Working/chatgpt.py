
from bs4 import BeautifulSoup
import requests
import csv
 

url = "https://weather.com/weather/tenday/l/USCA0987:1:US"
 

response = requests.get(url)
 

soup = BeautifulSoup(response.text, "html.parser")


forecast_container = soup.find(class_="DailyForecast--DisclosureList--nosQS")
 
dayData = []
forecast_data = []
allDays = forecast_container.find_all(class_='DetailsSummary--daypartName--kbngc')
allDays = str(allDays).replace('<h3 class="DetailsSummary--daypartName--kbngc" data-testid="daypartName">' , '').replace('</h3>', '').split(',')

allTemps = forecast_container.find_all(class_='DetailsSummary--temperature--1kVVp')

allTemps = str(allTemps).replace('[<div class="DetailsSummary--temperature--1kVVp" data-testid="detailsTemperature"><span class="DetailsSummary--highTempValue--3PjlX" data-testid="TemperatureValue">59°</span><span data-testid="lowTempValue">/<span class="DetailsSummary--lowTempValue--2tesQ" data-testid="TemperatureValue">' , '')
allTemps = allTemps.replace(' <div class="DetailsSummary--temperature--1kVVp" data-testid="detailsTemperature"><span class="DetailsSummary--highTempValue--3PjlX" data-testid="TemperatureValue">', '')
allTemps = allTemps.replace('</span></span></div>,', '').replace('</span><span data-testid="lowTempValue">/<span class="DetailsSummary--lowTempValue--2tesQ" data-testid="TemperatureValue">', '')
allTemps = allTemps.replace('</span></span></div>]', '')
allTemps = allTemps.split('°')

print(len(allTemps))
x = 1
i = 0
with open("forecast.csv", "w") as csv_file:
  while i <= 5:
    if x < len(allTemps):
      math =(int(allTemps[i]) + int(allTemps[x])) / 2
      dayData.append(allDays[i])
      dayData.append(math)
    else:
      pass

    csv_file.writelines(f'Day:{dayData[i]} Temp:{dayData[x]} | ')
    x +=2
    i +=1
############## i hate these comments ;-;