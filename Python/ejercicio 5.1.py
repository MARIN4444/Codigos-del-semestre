#ejercicio 5.1
"""
Created on Tue Mar  2 19:02:47 2021
determinar la media de una lista indefinida de numeros positivos, terminados con un numero negativo
@author: marin
"""
#programa que lee N numeros enteros y calcula su promedio sale con un numero menos a cero

#declarar variable
num= 0 #variable que almacena los numeros que digita el usuario
suma=0 #vaiable que almacena la suma de los numeros positivos
med=0.0 #variable que almacena la media
canEle=0 #variable que almacena la cantidad de numeros digitados

num = int(input("Numero: "))# lectura del primer numero

while (num > 0): #inicio del ciclo
    suma = suma+num
    num = int(input("Numero: ")) #lectura de los otros numeros
    cantEle = canEle + 1
    
#termina el ciclo
if canEle != 0:
    med = suma/canEle #calcular la media
    print("la media es: ", med)#imprimir la media
else:
    print("no hay numero para calcular la media")