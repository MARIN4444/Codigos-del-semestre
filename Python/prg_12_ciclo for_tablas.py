# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:37:10 2021

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

#inicio del ciclo
for conRepCiclo in range(multiplicador +1):
     resultado = tabla*conRepCiclo
     sumaResultado = sumaResultado + resultado
     print(tabla, "*", conRepCiclo, " = ", resultado)
     #incrementar la variable que controla el ciclo
#se imprime la suma po fuera del ciclo
print("la suma de los resultados es: ", sumaResultado)