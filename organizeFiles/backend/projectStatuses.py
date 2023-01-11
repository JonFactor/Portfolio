from pathlib import Path
import pathlib, os, shutil, sys, ast, traceback

notworking = []
working = []

workingDir = Path.cwd() / 'PRODUCT' / 'WORKING'
if os.path.exists(workingDir):
    shutil.rmtree(workingDir)
notworkingDir = Path.cwd() / 'PRODUCT' / 'NOT-WORKING'
if os.path.exists(notworkingDir):
    shutil.rmtree(notworkingDir)

for dir in os.listdir('Raw'):
    for file in os.listdir(f'Raw\\{dir}'):
        if '.py' in file:
            with open(f'Raw\\{dir}\\{file}') as f:
                source = f.read()
            Vaild = True
            try:
                ast.parse(source)
            except Exception:
                Vaild = False
            finally:
                if Vaild:
                    working.append(dir)
                else:
                    notworking.append(dir)


workingDir.mkdir(exist_ok=True)
notworkingDir.mkdir(exist_ok=True)

for work in working:
    workingDir = Path.cwd() / 'PRODUCT' / 'WORKING' / work

    workDir = f'Raw\\{work}'
    if not os.path.exists(workingDir):
        shutil.copytree(workDir,workingDir)

notworkingDir = Path.cwd() / 'PRODUCT' / 'NOT-WORKING'
notworkingDir.mkdir(exist_ok=True)

for notwork in notworking:
    notworkingDir = Path.cwd() / 'PRODUCT' / 'NOT-WORKING' / notwork

    notworkDir = f'Raw\\{notwork}'
    if not os.path.exists(notworkingDir):
        shutil.copytree(notworkDir,notworkingDir)
