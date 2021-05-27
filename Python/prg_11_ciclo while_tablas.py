# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:51:44 2021

@author: marin
"""

# programa que lee una tabla y la imprime desde el 1 hasta el 20 y suma el resultado

#declarar variables
tabla = 0
multiplicador = 1
resultado = 0
sumaResultado = 0
conRepCiclo = 1

#leer el numero de la tabla para la cual vamos a realizar las operaciones
tabla = int(input("Tabla: "))
#leer el multiplicador
multiplicador=int(input("Multiplicador: "))
#inicio del ciclo repetitivo WHILE
while(conRepCiclo <=multiplicador):
    resultado = tabla*conRepCiclo
    sumaResultado = sumaResultado + resultado
    print(tabla, "*", conRepCiclo, " = ", resultado)
    #incrementar la variable que controla el ciclo
    conRepCiclo = conRepCiclo +1
print("la suma de los resultadodos es: ", sumaResultado)