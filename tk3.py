# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 19:45:06 2023

@author: CristalAngel
"""

import tkinter as tk

def adiciona():
    i = lst.size()
    nome = txt.get()
    if len(nome) > 1:
        lst.insert(i+1,nome)
        txt.delete(0,"end")
    

app=tk.Tk()
app.geometry("400x200")

lbl = tk.Label(app,text="Insira um nome:")
lbl.place(x=10,y=10)

txt = tk.Entry(app)
txt.place(x=10,y=30)

btn = tk.Button(app, text="Adicionar >>", command=adiciona)
btn.place(x=150,y=25)

lst = tk.Listbox(app,width=19)
lst.pack(side=tk.RIGHT, fill=tk.Y)

app.mainloop()