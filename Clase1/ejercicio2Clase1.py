#se ingresa la cantidad de alumnos en un curso y la cantidad de mujeres, mostrar el porcentaje de hombres


print("ejercicio 2, porcentaje de hombres en clase")
valor_uno, valor_dos = 0, 0
while not (valor_uno * valor_dos):
    try:
        valor_uno = int(input("inserte la cantidad de alumnos del curso por favor: "))
        valor_dos = int(input("ingrese la cantidad de mujeres del curso por favor: "))

    except ValueError:
        print("te dije que metas valores numericos")

if (valor_uno - valor_dos) >= 0:
    print("el porcentaje de alumnos varones en el curso es de: ", ((valor_uno - valor_dos) / valor_uno) * 100, "%")
else:
    print("los datos ingresados estan mal, deberia ingresar primero la cantidad TOTAL de Alumnos luego, la cantidad de mujeres")
