# ejercicio 5.7
"""
Created on Tue Mar  2 18:24:07 2021
Leer notas de una clase de informatica y deducir todas aquellas que son Notables(7>= y <9)
@author: marin
"""
CantEst= int(input("ingrese el numero de estudiantes: "))

ContRep= 0

while(ContRep < CantEst):
    nombEst=str(input("ingrese el nombre del estudiante: "))
    not1=int(input("ingrese la primer nota: "))
    not2=int(input("ingrese la segunda nota: "))
    not3=int(input("ingrese la tercera nota: "))
    not4=int(input("ingrese la cuarta nota: "))
    
    promnot=not1+not2+not3+not4/4
    
    if 7>= promnot <9:
        print("Este estudiante es NOTABLE con una nota de ", promnot)
    
    ContRep = ContRep +1
    
    
    
