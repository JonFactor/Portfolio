import requests
import os
from pathlib import Path
from datetime import datetime
import time
import json
response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=o0U1fyym9QjCEarPABPI1Nuy40n5mGn0jmpmXxV2")

nasaImg = response.json()
print(nasaImg)
nasaImg = nasaImg['photos']


imgLinks = []

for i in range(len(nasaImg)):
    img = nasaImg[i]
    imgLinks.append(img["img_src"])
    i +=1

time1 = time.ctime().replace(':', '-') 
resultsDir = Path.cwd() / 'python'/'schoolWork'/'apis'/ f'result--{time1}'

w = 0
for w in range(len(imgLinks)):
    time1 = time.ctime().replace(':', '-')
    resultsDir = Path.cwd() / 'python'/'schoolWork'/'apis'/ f'result{time1}' / f'RESULT{w}'
    resultsDir.mkdir(parents=True, exist_ok=True)
    Path(resultsDir / "RESULTS.txt").write_text(str(imgLinks[w]))
    w += 1
