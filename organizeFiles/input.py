### imports
from pathlib import Path
import os, json
### functions
def inputs():
    global done, imports
    donetf = True
    while donetf:
        done = input('Sort By Working Status(Y/N):')
        if done == 'Y' or done == 'y':
            donetf = False
            done = True
        elif done == 'N' or done == 'n':
            donetf = False
            done = False
        else:
            print('Please Input Y or N')
    importstf = True
    while importstf:
        imports = input('Sort By Imports(Y/N):')
        if imports == 'Y' or imports == 'y':
            importstf = False
            imports = True
        elif imports == 'N' or imports == 'n':
            importstf = False
            imports = False
        else:
            print('Please Input Y or N')
def dictt():
    global data
    data = {
        'Done': done,
        'Imports' : imports
    }
def local():
    if os.path.exists('organizeFiles\localvars.json'):
        os.remove('organizeFiles\localvars.json')
    with open('organizeFiles\localvars.json', 'w') as x:
        x.writelines(json.dumps(data))
### function order
inputs()
dictt()
local()
### run mover
import moveing