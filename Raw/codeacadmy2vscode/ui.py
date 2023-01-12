### imports
import tkinter as tk
from tkinter import  ttk, Label,Entry,Button
import wave
### defining
ww = 500
wh = 700
backround ='#f2f3ba'
link = ''
Path = ''
### functions
def submit():
    with open('python\codeacadmy2vscode\local.txt', 'w') as loc:
        link = entLink.get()
        loc.writelines(link)
        loc.writelines('-----')
        loc.writelines(Path)
        if  link == '':
            print('oops')
            #wave.open('C:\\Users\jonfa\Documents\GitHub\Portfolio\python\codeacadmy2vscode\omg.mp3','r')
        else:
            menu.destroy()
### ui
try:
    menu = tk.Tk() # start
    menu.geometry(f"{ww}x{wh}")
    menu.configure(bg = backround)
    menu.title('CodeCadamy2VS')
    # defining
    lbltitle = Label()
    lblLink = Label()
    entLink = Entry()

    btnSubmit = Button()
    #configs
    lbltitle.configure(text='Code2VS',font=('Arial', 32), bg = backround)
    lblLink.configure(text='Link:',font=('Arial', 26), bg = backround)
    entLink.configure(textvariable=link,font=('Arial', 26), bg = backround)

    btnSubmit.configure(text='Submit',font=('Arial', 30),command=submit)
    #packing
    lbltitle.pack()
    lblLink.pack()
    entLink.pack()

    btnSubmit.pack()
finally:
    menu.mainloop() # end



import scraper