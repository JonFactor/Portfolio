import requests

response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=o0U1fyym9QjCEarPABPI1Nuy40n5mGn0jmpmXxV2")


print(response.json())
