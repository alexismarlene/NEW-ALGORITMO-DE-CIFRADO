# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:46:39 2019

@author: xxx
"""

from tkinter import *
import os

def funcion():
    
    os.system ("C:/Users/xxx/Downloads/tesis/Sin título0.py")
    
    root.iconify()

root = Tk()
boton = Button(root, text="Abrir otra ventana", command=funcion)
boton.pack()
root.mainloop()