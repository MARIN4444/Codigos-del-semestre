# ejercicio 116-funciones parametros
"""
Created on Sat Mar 13 14:39:10 2021

@author: marin
"""

#funcion

def mostrar_mensaje(mensaje):
    print("************************************************")
    print(mensaje)
    print("************************************************")
    
def carga_suma():
    valor1=int(input("ingrese el primer valor: "))
    valor2=int(input("ingrese el segundo valor: "))
    suma=valor1+valor2
    print(" ")
    print("la suma de los dos valores es: ", suma)

#programa principal
mostrar_mensaje("el programa calcula la suma de dos valores ingresados por teclado.")
carga_suma()
print(" ")
mostrar_mensaje("gracias por utilizar este programa")