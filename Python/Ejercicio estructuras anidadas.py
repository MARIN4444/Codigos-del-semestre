nombre=str(input("inserte nombre del estudiante:" ""))
nota1=int(input("inserter la primer nota: "))
nota2=int(input("inserte la segunda nota: "))
nota3=int(input("inserte la tercer nota: "))
prom=(nota1+nota2+nota3)/3
print(("El estudiante ")+(nombre)+(" ha tenido un rendimiento"))
if prom>=7:
    print("Alto")
else:
    if prom>=4:
        print("Regular")
    else:
        print("Bajo")
    