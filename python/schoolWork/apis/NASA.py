import requests
import json
responce = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY")

data = responce.json()
data = dict(data)
data = data['photos']
data = str(data)
data = data.split(',')
x=0
y = 6
q = 3
imgs = []
links = []
while x <= 4:
    if y <= len(data):
        imgs.append(data[y])
        y+=13


    imgs = str(imgs)
    imgs = imgs.split(':')
    if q <= len(imgs):
        links.append(imgs[q])
        q +=3
    x+=1
print(links)
