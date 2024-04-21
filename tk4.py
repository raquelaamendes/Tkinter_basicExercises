# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:27:19 2023

@author: CristalAngel
"""

from tkinter import filedialog
from tkinter import *
import webbrowser

 
def abrir_link():
    webbrowser.open("https://www.sapo.pt")

def abrirFic():
    f = filedialog.askopenfilename()
    print(f)
    f1 = open(f,"r")
    print(f1.read())
    f1.close()
    
    
    
app = Tk()
app.geometry("200x200")

btn = Button(app, text="Abrir ficheiro", command=abrirFic)
btn.pack()

b2 = Button(app, text="www.sapo.pt", command=abrir_link)
b2.pack()

app.mainloop()