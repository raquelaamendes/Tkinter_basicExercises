# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 19:00:49 2023

@author: CristalAngel
"""

import tkinter as tk

def dobro():
    n=txt1.get()
    lbl2.configure(text=float(n)*2)

app = tk.Tk()
app.geometry("400x100")

lbl1 = tk.Label(app, text="Insira um numero: ")
lbl1.grid(column=0, row=0, padx=15, pady=15)

txt1=tk.Entry(app, bd=5)
txt1.grid(column=1, row=0)

btn1 = tk.Button(app, text="Dobro", command=dobro)
btn1.grid(column=0, row=1)

lbl2=tk.Label(app,text="0")
lbl2.grid(column=1, row=1)


app.mainloop()
