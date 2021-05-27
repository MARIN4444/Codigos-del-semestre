# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:44:22 2021

@author: marin
"""
#Metodos de ordenamiento

#Crear lista y darle valores

listaBase=[34,12,45,2,37,60,34,8]

print("Lista Base: ", listaBase)
#Ordenar la lista con una funcion de python
listaBase.sort()
print("Lista Base Ordenada ascendentemente: ", listaBase)

#Odenar la lista con una funcion de python
listaBase.sort(reverse=True)
print("Lista base ordanada descendentemente: ", listaBase)

#===========================================
#Funcion desarrollada por el programador
#Ordenamiento burbuja ascendente
print("Funcon desarrollada por el progamador- Ascendente")
def ordenamientoBurbujaAscendente(unaLista):
    for numPasada in range(len(unaLista)-1, 0, -1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp=unaLista[i]
                unaLista[i]= unaLista[i+1]
                unaLista[i+1]= temp
                
unaLista = [54,26,93,17,77,31,44,55,20]
print("Lista Original: ", unaLista)

ordenamientoBurbujaAscendente(unaLista)
print("Lista Ordenada ascendente: ", unaLista)     
#==========================================
#Funcion desarrollada por el programador
#Ordenamiento burbuja descendente
print("Funcon desarrollada por el progamador- Descendente")
def ordenamientoBurbujaDescendente(unaLista):
    for numPasada in range(len(unaLista)-1, 0, -1):
        for i in range(numPasada):
            if unaLista[i]<unaLista[i+1]:
                temp=unaLista[i]
                unaLista[i]= unaLista[i+1]
                unaLista[i+1]= temp
            
unaLista = [54,26,93,17,77,31,44,55,20]
print("Lista Original: ", unaLista)


ordenamientoBurbujaDescendente(unaLista)
print("Lista Ordenada Descendente: ", unaLista)                
           

