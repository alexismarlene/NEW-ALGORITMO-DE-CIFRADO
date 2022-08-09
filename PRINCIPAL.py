from tkinter import *
import os
def function():
    
    os.system ("C:/Users/xxx/Downloads/tesis/ingreso1.py")
    root.iconify()
# Configuración de la raíz
root =Toplevel()
root.title("ACADEMIA TEKHNE SRL")
root.geometry("1200x600")
root.config(cursor="pirate")

frame = Frame(root, width=100, height=120)
img = PhotoImage(file="C:/Users/xxx/Downloads/tesis/logo-tekhne.gif")
Label(frame,image=img,bd=0).pack(side="left")
frame.pack(side=LEFT)
frame.pack(anchor=NW)
frame.config(cursor="pirate")
frame.config(bg="gray")
frame.config(bd=15)
frame.config(relief="sunken")




frame3 = Frame(root, width=0, height=0)
frame3.pack(padx=200,pady=200)

frame3.pack(side=RIGHT)
frame3.pack(anchor=S)
frame3.config(cursor="pirate")
frame3.config(bg="lightblue")
frame3.config(bd=15)
frame3.config(relief="sunken")
boton = Button(root,text="INGRESO",command=function)
boton.pack(side=LEFT)





root.config(cursor="arrow")
root.config(bg="gray")
root.config(bd=15)
root.config(relief="ridge")
# Finalmente bucle de la aplicación
root.mainloop()
