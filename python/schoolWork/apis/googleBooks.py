import requests
import os
from pathlib import Path
from datetime import datetime
import json
passed = False
while passed == False:
    query = input('Enter the book youd like to search')

    responce = requests.get(f"https://www.googleapis.com/books/v1/{query}/resourceID?parameters")

    if responce.status_code == '404':
        print('Book Does not exist')
    else:
        passed = True

results = responce.json()
results = str(results).split(',')
results = f'Volume: {results[5]} \n Title: {results[12]} \n Date: {results[3]} \n Description: {results[15]}'


### make files ###
time = str(datetime.now().strftime("%H:%M:%S"))
time = time.replace(':','_')
resultsDir = Path.cwd() / 'python'/'schoolWork'/'apis'/'books' / f'result_{time}'
resultsDir.mkdir(parents=True, exist_ok=True)

Path(resultsDir / "RESULTS.txt").write_text(str(results))