### imports
from pathlib import Path
import pathlib, os, shutil,json
### first things first
os.remove('organizeFiles\\byimportsTemp.json')
### grabbing
with open('organizeFiles/localvars.json', 'r') as loc:
    Bools = json.load(loc)
### functions
def ifdone():
    global baseDir
    if Bools['Done']:
        baseDir = Path.cwd() / 'PRODUCT' /'WORKING'
    else:
        baseDir = Path.cwd() / 'PRODUCT'
def writing():
    for dir in os.listdir('RAW'):
        for file in os.listdir(f'Raw\\{dir}'):
            if '.py' in file:
                with open(f'Raw\\{dir}\\{file}') as first, open('organizeFiles\\byimportsTemp.json', 'a') as second:
                    for line in first:
                        if not '#' in line:
                            if 'from' in line or 'import' in line:
                                tempdict = {
                                    'import' :line.replace('\n', ''),
                                    'file':file
                                }
                                second.write(json.dumps(tempdict))
                                second.write('\n')
def placeing():
    

###functionOrder
ifdone()
writing()
### finishing
