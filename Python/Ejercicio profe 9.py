#Ejercicio profe 9
"""
Calcular el sueldo total a recibir de un empleado.  El usuario deberá ingresar el número de horas trabajadas y
 el valor por cada hora. Considere en los cálculos el descuento de seguridad social y una bonificación del 2% 
 para aquellos cuyo sueldo no supere los 300 dólares.
"""
horas_trab=int(input("ingrese el numero de horas trabajadas: "))
valor_hora=int(input("ingrese el valor por hora: "))
sueldo_neto= horas_trab*valor_hora
seguridad_social= sueldo_neto/1.08

if seguridad_social<300:
     bonificacion=seguridad_social*1.02
     print("su suelto total es de ", bonificacion)
else: 
     print("su sueldo total es de ", seguridad_social)

