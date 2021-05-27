#Calculadora
"""
Calculadora creada usando la libreria tkinter
"""
from tkinter import Button , Tk, Entry

#Ventana
vent = Tk()
vent.title("Calculadora")
vent.geometry("400x350")


#entrada
ent_tex= Entry(vent, font=("calibri 28"))
ent_tex.place(relx=0.025, rely=0.03, relwidth=0.94, relheight=0.18 )

#Funciones
i =0

def click_boton(valor):
    global i
    ent_tex.insert(i, valor)
    i +=1
    
def borrar():
    ent_tex.delete(0, "end")
    i = 0
 
def hacer_operacion():
    ecuacion= ent_tex.get()
    resultado= eval(ecuacion)
    ent_tex.delete(0, "end")
    ent_tex.insert(0, resultado)
    i= 0     
    

    
     
#Botones
btn1 = Button(vent, text = "1", command= lambda: click_boton(1))
btn2 = Button(vent, text = "2", command= lambda: click_boton(2))
btn3 = Button(vent, text = "3", command= lambda: click_boton(3))
btn4 = Button(vent, text = "4", command= lambda: click_boton(4))
btn5 = Button(vent, text = "5", command= lambda: click_boton(5))
btn6 = Button(vent, text = "6", command= lambda: click_boton(6))
btn7 = Button(vent, text = "7", command= lambda: click_boton(7))
btn8 = Button(vent, text = "8", command= lambda: click_boton(8))
btn9 = Button(vent, text = "9", command= lambda: click_boton(9))
btn0 = Button(vent, text = "0", command= lambda: click_boton(0))
btnpunto = Button(vent, text = ".", command= lambda: click_boton("."))
btnresultado = Button(vent, text = "=", command= lambda: hacer_operacion())
btndivision = Button(vent, text = "/", command= lambda: click_boton("/"))
btnmultiplicacion = Button(vent, text = "X", command= lambda: click_boton("*"))
btnsuma = Button(vent, text = "+", command= lambda: click_boton("+"))
btnresta = Button(vent, text = "-", command= lambda: click_boton("-"))
btnborrar = Button(vent, text = "AC", command = lambda: borrar())
btnparentesis1= Button(vent, text = "(", command= lambda: click_boton("("))
btnparentesis2 = Button(vent, text = ")", command= lambda: click_boton(")"))
btnpotenciar = Button(vent, text = "^", command= lambda: click_boton("^"))

#Ubicaciones
btn0.place(relx=0.025 ,rely=0.77, relwidth=0.17, relheight=0.17 )
btnpunto.place(relx=0.21 ,rely=0.77, relwidth=0.17, relheight=0.17 )
btnresultado.place(relx=0.40 ,rely=0.77, relwidth=0.17, relheight=0.17 )
btnresta.place(relx=0.59 ,rely=0.77, relwidth=0.17, relheight=0.17 )
btnpotenciar.place(relx=0.78 ,rely=0.77, relwidth=0.17, relheight=0.17 )

btn1.place(relx=0.025 ,rely=0.59, relwidth= 0.17,relheight=0.17 )
btn2.place(relx=0.21 ,rely=0.59, relwidth=0.17,relheight=0.17 )
btn3.place(relx=0.40 ,rely=0.59, relwidth=0.17, relheight=0.17 )
btnsuma.place(relx=0.59 ,rely=0.59, relwidth=0.17, relheight=0.17 )
btnparentesis2.place(relx=0.78 ,rely=0.59, relwidth=0.17, relheight=0.17 )

btn4.place(relx=0.025 ,rely=0.41, relwidth=0.17, relheight=0.17 )
btn5.place(relx=0.21 ,rely=0.41, relwidth=0.17, relheight=0.17 )
btn6.place(relx=0.40 ,rely=0.41, relwidth=0.17, relheight=0.17 )
btnmultiplicacion.place(relx=0.59 ,rely=0.41, relwidth=0.17, relheight=0.17 )
btnparentesis1.place(relx=0.78 ,rely=0.41, relwidth=0.17, relheight=0.17 )

btn7.place(relx=0.025 ,rely=0.23, relwidth=0.17, relheight=0.17 )
btn8.place(relx=0.21 ,rely=0.23, relwidth=0.17, relheight=0.17 )
btn9.place(relx=0.40 ,rely=0.23, relwidth=0.17, relheight=0.17 )
btndivision.place(relx=0.59 ,rely=0.23 ,relwidth=0.17,relheight=0.17 )
btnborrar.place(relx=0.78 ,rely=0.23 ,relwidth=0.17,relheight=0.17 )

vent.mainloop()