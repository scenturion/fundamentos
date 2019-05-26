# dadas 3 listas de la misma longitud: nombre, parcial 1, parcial 2. 
# Cargar la lista con los apellidos y las notas de cada parcial, 
# el proceso termina con una 'f' en la variable nombre 
# validar que la nota se emcuentre entre 0 y 10
# informar, por fin de carga, cuantos alumnos rinden final con promedio entre 4 y 6

# MAtriz que guarda los 3 datos necesarios para poder trabajar
alumno=[]

primeraNota, segundaNota = -1, -1
alumnosFinal = 0

nombre = input("ingrese el nombre del alumno o f para salir: ")

while (nombre != "f") and (nombre != "F"):
    
    primeraNota = int(input("ingresar la nota del primer parcial, debe estar entre 0 y 10: "))
    while (primeraNota > 10) or (primeraNota < 0):
        primeraNota = int(input("ingresar la nota del primer parcial, debe estar entre 0 y 10: "))
    segundaNota = int(input("ingresar la nota del segundo parcial, debe estar entre 0 y 10: "))
    while (segundaNota > 10) or (segundaNota < 0):
        segundaNota = int(input("ingresar la nota del segundo parcial, debe estar entre 0 y 10: "))
    listaAux = [nombre, primeraNota, segundaNota]
    alumno.append(listaAux)
    nombre = input("ingrese el nombre del alumno o f para salir: ")

for i in range(0,len(alumno)):
    promedio = (alumno[i][1] + alumno[i][2]) / 2
    if (promedio >= 4) and (promedio <= 6) :
        print("el alumno: ", alumno[i][0], "rinde final, tiene un promedio de: ", promedio)
        alumnosFinal = alumnosFinal + 1

print("la cantidad de alumnos que rinden final son: ", alumnosFinal)
