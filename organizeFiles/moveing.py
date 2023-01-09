### imports
import os, json, shutil
from pathlib import Path
from datetime import date
### time
now = date.today()
### functions
def failSafe():
    if os.path.exists('Backups/AUTO-FAILSAFE'):
        shutil.rmtree('Backups/AUTO-FAILSAFE')
    shutil.copytree(os.getcwd(), 'Backups\AUTO-FAILSAFE')
def everything():
    if os.path.exists(Path.cwd() / 'EVERYTHING'):
        pass
    else:
        everythingdir = Path.cwd() / 'EVERYTHING'
        everythingdir.mkdir()
def done():
    if Bools['done']:
        pass

### localvars
with open('organizeFiles/localvars.json', 'r') as loc:
    Bools = json.load(loc)
    
### function order
failSafe()