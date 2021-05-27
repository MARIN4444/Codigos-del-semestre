"""Problema 7.1
Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos."""
num1=int(input("inserte el primer numero: "))
num2=int(input("inserte el segundo numero: "))
num3=int(input("inserte el tercer numero: "))
print("El numero mayor es ")
if num1>=num2 and num1>=num3:
    print(num1)
else:
    if num2>=num3:
        print(num2)
    else:
        print(num3)