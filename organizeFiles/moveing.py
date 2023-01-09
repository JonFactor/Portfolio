### imports
import os, json, shutil
from pathlib import Path
from datetime import date
### time
now = date.today()
### functions
def failSafe():
    shutil.copytree('C:\\Users\jonfa\Documents\GitHub\Portfolio', 'Backups\AUTO-FAILSAFE')
def RAW():
    if os.path.exists(Path.cwd() / 'RAW'):
        shutil.rmtree(f'{Path.cwd()} / RAW')

    everythingdir = Path.cwd() / 'RAW'
    everythingdir.mkdir()
    shutil.copytree('')
def done(): 
    if Bools['done']:
        pass

### localvars
with open('organizeFiles/localvars.json', 'r') as loc:
    Bools = json.load(loc)

### function order
#failSafe()
RAW()