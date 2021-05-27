#Calcular área y perímetro para un triángulo equilatero.

a=input("ingrese el lado 1: ")
a=float(a)
b=input("ingrese el lado 2: ")
b=float(b)
c=input("ingrese el lado 3: ")
c=float(c)

#semiperimetro
p=(a+b+c)/2

A=(p*(p-a)*(p-b)*(p-c))**(1/2)

#muestra el area
print("el area del triangulo es de:",A)