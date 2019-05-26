# dadas 3 listas de la misma longitud: nombre, parcial 1, parcial 2. 
# Cargar la lista con los apellidos y las notas de cada parcial, 
# el proceso termina con una 'f' en la variable nombre 
# validar que la nota se emcuentre entre 0 y 10
# informar, por fin de carga, cuantos alumnos rinden final con promedio entre 4 y 6

nombreAlumno=[]
primerParcial=[]
segundoParcial=[]
rindeFinal=[]
promedio=[]
primeraNota, segundaNota = -1, -1
alumnosFinal = 0

nombre = input("ingrese el nombre del alumno o f para salir: ")

while (nombre != "f") and (nombre != "F"):
    nombreAlumno.append(nombre)
    primeraNota = int(input("ingresar la nota del primer parcial, debe estar entre 0 y 10: "))
    while (primeraNota > 10) or (primeraNota < 0):
        primeraNota = int(input("ingresar la nota del primer parcial, debe estar entre 0 y 10: "))
    segundaNota = int(input("ingresar la nota del segundo parcial, debe estar entre 0 y 10: "))
    while (segundaNota > 10) or (segundaNota < 0):
        segundaNota = int(input("ingresar la nota del segundo parcial, debe estar entre 0 y 10: "))
    primerParcial.append(primeraNota)
    segundoParcial.append(segundaNota)
    promedioResultante = (primeraNota+segundaNota)/2

    promedio.append(promedioResultante)
    if (promedioResultante >= 4 ) and (promedioResultante <= 6):
        rindeFinal.append('si')

    else:
        rindeFinal.append('no')

    nombre = input("ingrese el nombre del alumno o f para salir: ")

for i in range(0,len(nombreAlumno)):
    if rindeFinal[i] == 'si':
        print("el alumno: ", nombreAlumno[i], "rinde final, tiene un promedio de: ", promedio[i])
        alumnosFinal = alumnosFinal + 1

print("la cantidad de alumnos que rinden final son: ", alumnosFinal)
