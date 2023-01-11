### imports
from pathlib import Path
import os, shutil
### vars
pydictionary = {}
pydir = []
notpydir = []
defaultDir = Path.cwd() / 'PRODUCT'
RawDir = Path.cwd() / 'Raw'
extention = 'py'
### functions
def settup():
    global PyDir, NotPyDir, TypeDir
   
    TypeDir = defaultDir / 'BY-TYPE'
    shutil.rmtree(TypeDir)
    TypeDir.mkdir(parents=True, exist_ok=True)
    PyDir = TypeDir / extention
    PyDir.mkdir(parents=True, exist_ok=True)
    NotPyDir = TypeDir / f'NOT-{extention}'
    NotPyDir.mkdir(parents=True, exist_ok=True)
def workplz():
    for dir in os.listdir('RAW'):
        py = 0
        rawDir = f'Raw\\{dir}'
        for file in os.listdir(rawDir):
            fileex = os.path.splitext(file)
            if extention in fileex[1]:
                py +=1
            else:
                pass
        if py > 0:
            ex = extention
        else:
            ex = f'NOT-{extention}'
        both = Path.cwd() / 'PRODUCT' / 'BY-TYPE' / ex / dir  
        if not os.path.exists(both) :
            shutil.copytree(rawDir, both)
        else:
            pass
                

### function order

settup()
workplz()
### test

