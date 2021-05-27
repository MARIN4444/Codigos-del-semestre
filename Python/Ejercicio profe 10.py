#Ejercicio profe 10
"""
Calcular las raíces de una ecuación cuadrática.  Suponga que los datos ingresados no generan raíces imaginarias.
"""

from math import sqrt
a=int(input("inserte el coeficiente de a: "))
b=int(input("inserte el coeficiente de b: "))
c=int(input("inserte el coeficiente de c: "))
   
if (pow(b,2)-4*a*c)<0:
    print("La solucion de la operacion genera raices imaginarias")
    
else:
    raizpositiva=(-b+sqrt(pow(b,2)-4*a*c))/2*a
    raiznegativa=(-b-sqrt(pow(b,2)-4*a*c))/2*a

    print("Las soluciones de la ecuacion son ")
    print(raizpositiva)
    print(raiznegativa)
 