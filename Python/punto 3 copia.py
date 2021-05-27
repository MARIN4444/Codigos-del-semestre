#punto 3
"""
• las horas inferiores o iguales a 35 horas (normales) se pagan a una tarifa determinada que se debe introducir por 
teclado al igual que el número de horas trabajadas, el nombre del trabajador, género  y 1,2 o 3 de acuerdo a la sección 
donde trabaje
• las horas superiores a 35 se pagarán como extras a un promedio de 1,5 horas normales,
• los impuestos a deducir a los trabajadores varían en función de su sueldo mensual:
  Salud 12,5% del salario
  ICBF 4% del salario
  Retención en la fuente según la tabla anexa:
       de 2’000.000 a 3´000.000 5%
       de 3’000.001 a 4’000.000 7%
       de 4’000.001 a 5’000.000 9%
       de 5’000.000 en adelante 11%
Imprima el desprendible de pago detallado para cada empleado
Imprima la planilla de totales de pago de la empresa (Total Empleados, Total Horas, Total extras, pago horas, 
                                                      pago extras, etc)	
Imprimir la planilla de totales los acumulados por sección.
Imprimir la planilla de totales los acumulados por género.
"""
#variables 
terminar=""
cant_trabajadores=0
cant_horas=0
cant_horas_extra=0
pago_horas=0
pago_horas_extra=0
pago_total_extra=0
masculino=0
femenino=0
seccion=0
sec_1=0
sec_2=0
sec_3=0

#funcion definida para establecer la impresion de los datos solicitados 
def desprendible_82202114100_82202114054_82202114635():
    print("************************************************")#espaciador
    print("nombre: ", nombre)
    print("seccion: ", seccion)
    print("horas: ", horas)
    print("tarifa: ", tarifa)
    print("************************************************")
    print("el total de trabajores es de: ", cant_trabajadores)
    print("horas totales: ", cant_horas)
    print("horas extra totales: ", cant_horas_extra)
    print("total pagado", pago_horas)
    print("total pagado por horas extra: ", pago_horas_extra)
    print("total pagado con horas extra: ", pago_total_extra)
    print("************************************************")
    print("el total de trabajadores en la seccion 1 es: ", sec_1)
    print("el total de trabajadores en la seccion 2 es: ", sec_2)
    print("el total de trabajadores en la seccion 3 es: ", sec_3)
    print("************************************************")
    print("el numero total de hombres es: ", masculino)
    print("el numero total de mujeres es: ", femenino)
    print("************************************************")
    
    
    
    
#funcion definida para para calcular el impuesto y retencion sobre el sueldo mensual    
def imp_retencion_82202114100_82202114054_82202114635():
    imp_salud=tarifa_total*0.125
    imp_ICBF=tarifa_total*0.04
    tarifa_imp=tarifa_total-imp_salud-imp_ICBF
    
    if tarifa_imp<2000000:
        retencion=tarifa_imp
        print("************************************************")
        print("pago total: ", retencion)
        desprendible_82202114100_82202114054_82202114635()
    
    else:
        
        if tarifa_imp<=3000000:
            retencion=tarifa_imp/1.05
            print("************************************************")
            print("pago total: ", retencion)
            desprendible_82202114100_82202114054_82202114635()
        
        else:
        
            if 3000000<tarifa_imp and tarifa_imp<=4000000:
                retencion=tarifa_imp/1.07
                print("************************************************")
                print("pago total: ", retencion)
                desprendible_82202114100_82202114054_82202114635()
            
            else:
        
                if 4000000<tarifa_imp and tarifa_imp<5000000:
                    retencion=tarifa_imp/1.09
                    print("************************************************")
                    print("pago total: ", retencion)
                    desprendible_82202114100_82202114054_82202114635()
                
                else:
    
                    if 500000<=tarifa_imp:
                        retencion=tarifa_imp/1.11
                        print("************************************************")
                        print("pago total: ", retencion)
                        desprendible_82202114100_82202114054_82202114635()
                    
#Inicio del ciclo
while 1:
    
    #variables ingresadas por teclado
    nombre=str(input("ingrese el nombre del trabajador: "))
    horas=float(input("ingrese las horas trabajadas: "))
    tarifa=int(input("ingrese la tarifa por hora: "))
    seccion=int(input("ingrese la seccion a la que pertenece: "))
    genero=int(input("seleccione un genero: hombre= 1, mujer= 2 : "))
    
    #proceso para calcular la cantidad total de trabajadores por seccion
    if seccion== 1:
        sec_1=sec_1+1
    
    if seccion == 2:
        sec_2=sec_2+1
    
    if seccion == 3:
        sec_3=sec_3+1
        
    #proceso para calcular la cantidad total de trabajadores por genero
    if genero == 1:
        masculino=masculino+1
        
    if genero ==2:
        femenino=femenino+1
    
    
    #procesos para calcular la cantidad total de: trabajadores, horas, horas extra, pagos, pagos horas extra
    cant_trabajadores=cant_trabajadores+1
    cant_horas=cant_horas+horas
    pago=tarifa*horas
    pago_horas=pago_horas+pago
    pago_horas_extra=(horas-35)*(1.5*tarifa)
    pago_total_extra=pago_total_extra+(pago+pago_horas_extra)
    
    
    
    #condicion que verifica si no se deben pagar horas extra
    if horas<=35:
        tarifa_total=horas*tarifa
        imp_retencion_82202114100_82202114054_82202114635()

    
    #condicion que verifica si se deben pagar horas extra       
    if horas>35:
        tarifa_total=(horas*tarifa)+(horas-35)*(1.5*tarifa) 
        horas_extra=horas-35
        cant_horas_extra=cant_horas_extra+horas_extra
        imp_retencion_82202114100_82202114054_82202114635()
        
    
   #variable que se usa para terminar el ciclo
    terminar=str(input("si desea acabar escriba (salir), de lo contrario escriba (continuar): "))
    
    if terminar == "salir":
        break

    
    
  
        
    
    
    
 



