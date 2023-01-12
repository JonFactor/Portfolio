### imports
import os, json, shutil
from pathlib import Path
from datetime import date
### time
now = date.today()
### functions
def failSafe():
    if os.path.exists('Backups\AUTO-FAILSAFE'):
        pass
    else:
        shutil.copytree('Backups\MANUAL-FAILSAFE', 'Backups\AUTO-FAILSAFE')
def RAW():
    if os.path.exists(Path.cwd() / 'RAW'):
        shutil.rmtree(f'{Path.cwd()}\RAW')
    else:
        pass

    shutil.copytree('Backups\AUTO-FAILSAFE','Raw')
def Product():
    if os.path.exists(Path.cwd() / 'PRODUCT'):
        shutil.rmtree(f'{Path.cwd()}\PRODUCT')
    else:
        pass
    
    productDir = Path.cwd() / 'PRODUCT'
    productDir.mkdir(exist_ok=True)

def ifs(): 
    if Bools['Done']:
        import projectStatuses
    else:
        pass
    if Bools['Imports']:
        import byimports
    else:
        pass
    if Bools['Type']:
        import byType
    else:
        pass

### localvars
with open('organizeFiles/localvars.json', 'r') as loc:
    Bools = json.load(loc)
### function order
failSafe()
RAW()
Product()
ifs()