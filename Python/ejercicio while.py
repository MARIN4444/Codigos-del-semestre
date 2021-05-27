# Ejercicio con while
"""
Created on Thu Mar 11 19:09:27 2021

@author: marin
"""

#Programa que calcula el cuadrado de los primeros 100 numeros

#Area de declaracion de variables
contadorRepeticiones=1
cuadradonumero=0
acumuladorsuma=0
num=1

#Entradas
Cantidadnumeros=int(input("Cantidad de numeros: "))
#Procesos
#Ciclo para de 1 hasta 100
while contadorRepeticiones <= Cantidadnumeros:
#for num in range(1,Cantidadnumeros+1,1):
    cuadradonumero=contadorRepeticiones*contadorRepeticiones
    acumuladorsuma=acumuladorsuma+cuadradonumero
    print("El cuadrado de: ", contadorRepeticiones," es ", cuadradonumero)
    print("La suma acumulada es: ", acumuladorsuma)
    contadorRepeticiones=contadorRepeticiones+1
#fin del ciclo

print("La suma de los cuadrados es: ", acumuladorsuma)