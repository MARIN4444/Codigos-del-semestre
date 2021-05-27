# ejercicio profe 3
"""
Realice un programa que obtenga el índice de masa corporal de una persona, ingresando la estatura en centímetros y el peso en kilos.
"""

estatura=int(input("ingrese la estatura en centimetros: "))
peso=float(input("ingrese el peso en kilos: "))
metros= estatura/100
indice_masa= peso/pow(metros,2)
print("su indice de masa corporal es de ", indice_masa)

