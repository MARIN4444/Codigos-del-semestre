# Ejercicios Tkinter
"""
usar la libreria Tkinter para crear ventanas y botones
"""
from tkinter import* #Label=ingresar texto en ventana, #Tk=crear ventana, Button=crear botones

def miFuncion():
    print("Este mensaje es del boton")


ventana = Tk() #crear la ventana
ventana.title("Hola mundo") #agregar titulo a la ventana
ventana.geometry("400x200") #agregar dimenciones a la ventana

lbl =Label(ventana, text="este es un label")
lbl.pack()

btn = Button(ventana, text="Presionar", command =miFuncion)
btn.config(fg="brown", bg="yellow") #cambiar propiedades
btn.pack()

ventana.mainloop()

""" 
Para ejecutar solo la ventana debemos guardarlo en .pyw
"""