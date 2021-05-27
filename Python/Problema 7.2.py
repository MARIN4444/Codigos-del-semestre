"""Problema 7.2
Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)"""
num=int(input("ingrese un numero: "))
print("el numero ingresado es ")
if num>=1:
    print("Positivo")
else:
    if num<=-1:
        print("Negativo")
    else:
        print("Nulo")
