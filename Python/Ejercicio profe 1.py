#Ejercicio profe 1
"""
Calcular el valor a pagar de una compra realizada, cuyo monto neto es ingresado por el usuario. Considere que el valor del 
IVA (Impuesto al Valor Agregado- puede variar en cada país), y un descuento del 5% para todas las compras.
"""

compra=int(input("ingrese el valor neto de la compra: "))
IVA= compra*1.19
descuento= int(IVA/1.05)
descuento=str(descuento)
print("Debe pagar "+ descuento)