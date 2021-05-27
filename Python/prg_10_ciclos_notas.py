#programa que calcula la nota de un estudiante

#entradas
#pedir el nombre del estudiante y sus 3 notas de parciales

canEst=int(input("cantidad de estudiantes: "))

#inicializar la variable que controla el ciclo
contRep=0

#variable para calcular la nota promedio del grupo
sumDefGru=0.0

while(contRep < canEst):
    # Instrucciones a repetir
    nomEst=input("Nombre estudiante: ")
    notUnoEst=float(input("parcial uno: "))
    notDosEst=float(input("parcial dos: "))
    notTresEst=float(input("parcial tres: "))
    
    #calculos

    notDefEst= (notUnoEst+notDosEst+notTresEst)/3
    
    #acumulo las definitivas del grupo
    sumDefGru=sumDefGru+notDefEst

    #imprimir los resultados - salida

    print(f"la nota definitiva es : {notDefEst:.2f}")
    
    #incrementar la varibable que controla el ciclo
    
    contRep = contRep+1
    
#calcular el promedio del grupo

notProDefGru = sumDefGru/canEst

#imprimir la nota promedio del grupo
print(f"2. la nota promedio del grupo es: {notDefEst:.2f}")
