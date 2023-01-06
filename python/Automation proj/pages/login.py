import tkinter as tk
from ctypes import windll
from tkinter.ttk import Label, Entry, Button
##### imports ######
try:
    #### Starting #####
    window = tk.Tk()
    #### fix blurr ####
    windll.shcore.SetProcessDpiAwareness(1)
    #### title ####
    window.title('Login')
    #### window size ####
    windowW = 600
    windowH = 900
    #### screen size ####
    screenW = window.winfo_screenmmwidth()
    screenH = window.winfo_screenheight()
    #### screen center #### 
    centerX = int(screenW / 2 - windowW / 2)
    centerY = int(screenH / 2 - windowH / 2)
    #### setting window size ####
    window.geometry(f'{windowW}x{windowH}+{centerX}+{centerY}')
    #### make resizable ####
    window.resizable(windowW,windowH)
    #### msc attributes ####
    #### transfarency ####
    window.attributes('-alpha',1)
    #### order ####
    window.attributes('-topmost',1)
    #up window.lift()
    #down window.lower()
    #### icon ####
    window.iconbitmap('python\Automation proj\images\Screenshot 2023-01-04 111710.ico')
    #### Body #####
    #title
    lblmessage = Label(window, text="Login Here", font=("Helvetica", 36))
    lblmessage.pack(ipadx=10, ipady=10)
    #ID
    varID = ''
    lblID = Label(window, text='ID:', font=("Helvetica", 18))
    lblID.pack(ipadx=10, ipady=10)
    entID = Entry(window, textvariable=varID, font=("Helvetica", 18))
    entID.pack()
    #Submit
    btnSub = Button(window, text='Submit', )
    

finally:
    window.mainloop()

    #### after ####