# Ejercicio que almacena en listas - proceso en funciones
# Declarar las librerias a usar para la solucion

import matplotlib.pyplot as plt

# Generar las listas con los datos inicializados
nombreProducto=["ron","aguardiante","vino","cerveza","tequila"]
existenciaProducto=[75,50,100,150,40]

# Funciones que resuelven el problema

def f_calc_tot_existencias():
    sumaExistencias=0
    for posLis in range(4):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    print("Total Existencias: ",sumaExistencias)
    
    
def f_calc_tot_existencias_2():
    sumaExistencias=0
    for posLis in range(len(existenciaProducto)):
        sumaExistencias=sumaExistencias+existenciaProducto[posLis]
    return(sumaExistencias)

def f_calc_prom_existencias():
    promExistencias =f_calc_tot_existencias_2()/len(existenciaProducto)
    return(promExistencias)

# Llamado a las funciones que realizan los calculos
f_calc_tot_existencias()
print("Total Existencias 2: ",f_calc_tot_existencias_2())
print("Promedio de Existencias: ",f_calc_prom_existencias())
# Grafica la informacion
fig, ax = plt.subplots()
# Definir el titutlo del Grafico
ax.set_title("Grafico de existencias del producto")
ax.set_xlabel("productos")
ax.set_ylabel("existencias")

# Crear el grafico
plt.bar(nombreProducto, existenciaProducto)

# Publico el Grafico
plt.show()