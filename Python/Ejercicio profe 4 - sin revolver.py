# ejercicio profe 4
"""
 Realice un programa que obtenga la calificación que debe obtenerse en un examen supletorio, si se conoce que el promedio incluido el supletorio
 para aprobar debe ser mínimo de 3.5 . El usuario debe ingresar las calificaciones en números enteros del primer y segundo bimestre.
"""

bimestre1=int(input("inserte la calificacion del primer bimestre: "))
bimestre2=int(input("inserte la calificacion del segundo bimestre: "))
promedio1=2*((bimestre1+bimestre2)/2)
nota_final=(bimestre1+bimestre2)/2+(promedio1/2)
supletorio=(bimestre1+bimestre2+promedio1)/3
print(promedio1)
print("calificacion necesaria ", supletorio)



