### imports
from pathlib import Path
import pathlib, os, shutil,json
### first things first
if os.path.exists('PRODUCT\BY-IMPORTS'):
    shutil.rmtree('PRODUCT\BY-IMPORTS')


baseDir = Path.cwd() / 'PRODUCT' / 'BY-IMPORTS'
baseDir.mkdir(exist_ok=True,parents=True)
### functions

def working():
    filelist = []
    for dir in os.listdir('RAW'):
        rawDir = f'Raw\\{dir}'
        for file in os.listdir(rawDir):
            if '.py' in file:
                filelist.append(file)

                for line in open(f'Raw\\{dir}\\{file}'):
                    if not '#' in line:
                        if 'import' in line:

                            line2 = line.replace('\n', '').replace(' ','-')
                            filedir = baseDir / line2 
                            if not os.path.exists(filedir):
                                filedir.mkdir(exist_ok=True,parents=True)

                        else:
                            noimportdir = baseDir / 'NO IMPORTS'
                            if not os.path.exists(baseDir / 'NO IMPORTS'):
                                noimportdir.mkdir(exist_ok=True,parents=True)
                if line in file:
                    filelist.append(dir)
                for filee in filelist:
                    if not os.path.exists(filedir/dir):
                        shutil.copytree(rawDir, filedir/dir)


def refine():
    for dir in os.listdir('PRODUCT\BY-IMPORTS'):
        Dir = f'PRODUCT\BY-IMPORTS\\{dir}'
        isempty = os.stat(Dir)
        isempty = isempty.st_size
        
        if os.path.exists(Dir):
            if isempty == 0:
                try:
                    os.rmdir(Dir)
                except Exception:
                    pass
###functionOrder
working()
refine()
### finishing
