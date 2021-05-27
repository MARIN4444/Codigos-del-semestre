#punto 1
"""
Calcular el área y el perímetro 
"""

import math
#Calcular área y perímetro para un triángulo equilatero.

#Funcion para calcular el area de un triangulo.
lado=int(input("ingrese el lado del triangulo: "))

def indicar_area_82202114100_82202114054_82202114635():
  area=(math.sqrt(3)/4)*pow(lado, 2)
  print(area)

#Funcion para calculara el perimetro de un triangulo.
def indicar_perimetro_82202114100_82202114054_82202114635(lado):
  perim = lado + lado + lado
  print("El Perimetro es", perim) 

#Funcion para cargar los datos en el sistema.
def llenar_datos_82202114100_82202114054_82202114635():
  
  print("considerando que un triangulo equilatero \n" 
        "tiene sus 3 lados iguales, dejaremos un valor de 4 a la base")

indicar_area_82202114100_82202114054_82202114635()
indicar_perimetro_82202114100_82202114054_82202114635(lado)

llenar_datos_82202114100_82202114054_82202114635()