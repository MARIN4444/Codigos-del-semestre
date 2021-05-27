# Ejercicio profe 6
"""
  Realice un programa que resuelva lo siguiente: Si n Empleados  realizan una actividad en k horas, ¿cuántos empleados se necesitarán
  para realizar la misma actividad en k1 horas?
"""
empleados=int(input("inserte el numero de empleados: "))
horas=int(input("inserte las horas: "))
nuevas_horas=int(input("inserte el nuevo numero de horas: "))
empleados_necesarios= (empleados*nuevas_horas)/horas
print("se necesitan ", empleados_necesarios, " empleados para realizar la misma actividad en ", nuevas_horas, "horas")
    
    
