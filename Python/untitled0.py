# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:22:59 2021

@author: marin
"""
matrizNumeros=[[7,8,3],[1,9,2],[4,6,5]]

print(matrizNumeros)

#Suma de todos los elementos de la matriz

sumEleMat=0
for f in range (3):
    for c in range (3):
        sumEleMat=sumEleMat+matrizNumeros[f][c]

print("La suma de los elementos es: ", sumEleMat)

#Imprimir la matriz
sumDiaPri=0
for pos in range (3):
    sumDiaPri=sumDiaPri+matrizNumeros[pos][pos]
print("Diagonal Principal: ", sumDiaPri)

        
