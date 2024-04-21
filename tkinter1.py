# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 22:25:04 2023

@author: CristalAngel
"""

import tkinter

def ola():
    lbl["text"] = "Olá, Boa Noite!!!"

app = tkinter.Tk()

app.title("A minha janela")

app.geometry("300x100")

lbl = tkinter.Label(app, text="Formação em Python", font=("Arial", 21), bg="yellow",fg="red")
lbl.pack()

b1 = tkinter.Button(app,text="Clica me",fg="#00FF00",command=ola)
b1.pack()

txt = tkinter.Entry(app, width=21)
txt.pack()

app.mainloop()