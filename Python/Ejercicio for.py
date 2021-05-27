#Ejercicio con for
"""
Created on Thu Mar 11 18:48:40 2021

@author: marin
"""
#Programa que calcula el cuadrado de los primeros 100 numeros

#Area de declaracion de variables
cuadradonumero=0
acumuladorsuma=0
num=1

#Entradas
Cantidadnumeros=int(input("Cantidad de numeros: "))
#Procesos
#Ciclo para de 1 hasta 100
for num in range(1,Cantidadnumeros+1,1):
    cuadradonumero=num*num
    acumuladorsuma=acumuladorsuma+cuadradonumero
    print("El cuadrado de: ", num," es ", cuadradonumero)
    print("La suma acumulada es: ", acumuladorsuma)
#fin del ciclo

print("La suma de los cuadrados es: ", acumuladorsuma)