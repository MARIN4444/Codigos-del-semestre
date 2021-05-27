# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:47:22 2021

@author: marin
"""
NomAlumn = ""
CalBASIC = 0.0
CalPascal = 0.0
CalFORTRAN = 0.0
ContRep = 1
Media = 0.0
Terminar = ""
CantAlumnTotal = 0

opcion=int(input("opcion 1 para hacerlo con una cantidad; opcion 2 para hacerlo libre: "))

if opcion == 1:
    
    CantAlumn = int(input("Cantidad de alumnos: "))

    while (ContRep <= CantAlumn ):
        NomAlumn= str(input("Nombre del Alumno: "))
        CalBASIC= float(input("calificacion de la asignatura BASIC: "))
        CalPascal= float(input("calificacion de la asignatura Pascal: "))
        CalFORTRAN= float(input("calificacion de la asignatura FORTRAN: "))
        Media = (CalBASIC + CalPascal + CalFORTRAN)/3
        ContRep= ContRep + 1
        print("La media del alumno ",NomAlumn+", es de: ",Media)
        
else:
    if opcion == 2:
        while 2:

            NomAlumn= str(input("Nombre del Alumno: "))
            CalBASIC= float(input("calificacion de la asignatura BASIC: "))
            CalPascal= float(input("calificacion de la asignatura Pascal: "))
            CalFORTRAN= float(input("calificacion de la asignatura FORTRAN: "))
            Media = (CalBASIC + CalPascal + CalFORTRAN)/3
            CantAlumnTotal= CantAlumnTotal + 1
            print("La media del alumno ",NomAlumn+", es de: ",Media)
            Terminar=str(input("si desea terminar escriba (salir): "))
            if Terminar == "salir" or "Salir":
                print("la lista a terminado")
                print("cantidad de alumnos es :", CantAlumnTotal)
                break
                       
    else:
        print("cantidad de alumnos :", CantAlumnTotal)
        print("No has introducion una opcion valida")
    

    