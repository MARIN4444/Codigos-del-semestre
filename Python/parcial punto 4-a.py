#punto 4-a
"""
leer un número entero e imprima la serie fibonacci hasta x término
"""

#entrada
termino_limite = int(input("Ingrese un numero para límite máximo de la sucesión: "))


def fib(n):
    a, b = 0, 1
    for i in range(termino_limite):
        print(a, end=' ')
        a, b = b, a + b
      
#salida
print(fib(termino_limite))
   