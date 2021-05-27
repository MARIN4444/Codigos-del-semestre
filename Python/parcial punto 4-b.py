# punto 4-b


#leer un número entero e imprima cual es el valor de ese término en la serie
n2=int(input("Ingrese el valor que quiere encontrar: "))
def fib(n2):
    a = 0
    b = 1
    
    for k in range(n2):
        c = b+a
        a = b
        b = c
        
    return a
fib(n2)
print(fib(n2))