import tkinter as tk
from ctypes import windll
##### imports ######
try:
    #### Starting #####
    window = tk.Tk()
    #### fix blurr ####
    windll.shcore.SetProcessDpiAwareness(1)
    #### title ####
    window.title('WebScraper')
    #### size ####
    window.geometry('700x500+50+50')
    #### Body #####
    Title = tk.Label(window, 'BOOBS', font='')
    

finally:
    window.mainloop()

    #### after ####