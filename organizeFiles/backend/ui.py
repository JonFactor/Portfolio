import tkinter as tk
from ctypes import windll
from tkinter import Button
##### imports ######
### defining
work = False
### functions
def wokring():
    work = True
try:
    #### Starting #####
    window = tk.Tk()
    #### fix blurr ####
    windll.shcore.SetProcessDpiAwareness(1)
    #### tool bar ####
    window.config(menu="")
    #### title ####
    window.title('Organize')
    

    #### size ####
    ww = 150
    wh = 50
    #### screen size ####
    screenW = window.winfo_screenmmwidth()
    screenH = window.winfo_screenheight()
    #### screen center #### 
    centerX = int(screenW / 2 - ww / 2)
    centerY = int(screenH / 2 - wh / 2)
    #### screen size ####
    window.geometry(f'{ww}x{wh}+{centerX}+{centerY}')
    #### Body #####
    Working = Button()
    ### config
    Working.config(text='Working',command=wokring())
    ### pack
    Working.pack()

finally:
    window.mainloop()

    #### after ####
import inputs