"""Problema 7.4
Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total de preguntas que 
se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa que ingrese los dos datos 
por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido"""

preguntastotales=int(input("Ingresa la cantidad total de preguntas: "))
preguntascorrectas=float(input("Ingrese la cantida de preguntas correctas: "))
porcentajes=(preguntascorrectas*100)/preguntastotales
if porcentajes>=90:
    print("Nivel maximo")
else:
    if porcentajes>=75:
        print("Nivel medio")
    else:
        if porcentajes>=50:
            print("Nivel regular")
        else:
            print("Fuera de nivel")
