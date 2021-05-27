#punto 4-c

#variable
suma=0

#funcion definida que sirve para desarrollar la formula de fibonacci
def fib(n):
    if n < 2:
        return n
    else:
        # ecuacion de fibonacci fn= fn-1 + fn-2
        return fib(n-1) + fib(n-2)
#datos de entrada  
primer_valor=int(input("ingrese el primer valor: "))
segundo_valor=int(input("ingrese el segundo valor: "))
segundo_valor=segundo_valor+1 #se le suma 1 para que en el rango coja de extremo a extremo
a=range (primer_valor, segundo_valor)

#se usa un ciclo for para ir imprimiendo y sumando los valores dados por la funcion definida
for x in a:
    print(fib(x))
    
    suma=suma+fib(x)
    
print("la suma de los valores del rango es: ", suma)

