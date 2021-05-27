"""Problema 7.3
Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor."""
num=int(input("ingrese un numero: "))
print("su numero es de ")
if num>=-9 and num<10:
    print("una cifra")
else:
    if num>=-99 and num<100:
        print("dos cifras")
    else:
        if num>=-999 and num<1000:
            print("tres cifras")
        else:
            print("Error")
