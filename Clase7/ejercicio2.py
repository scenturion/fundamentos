# Se desea determinar una serie de datos estadísticos en un curso de Programación I, al fin de la cursada
# Para ello se ingresa la LU del alumno, la nota del parcial 1 y la nota del parcial 2.
# El fin del ingreso se indica ingresando un cero en el campo LU
# Informar: Cuántos alumnos aprobaron los dos parciales y que porcentaje representa este dato?. 
# Qué porcentaje recupera el primero, cuántos deben recuperar los dos y cuántos recuperan el segundo.?  Cantidad de alumnos del curso.

totalAlumnos = 0
aprobados = 0
recuperaPrimero = 0
recuperaSegundo = 0
recuperaAmbos = 0
legajo = int(input("ingrese el legajo del alumno: "))
while legajo != 0:
    parcialUno = int(input("ingrese la nota del primer parcial: "))
    parcialDos = int(input("ingrese la nota del segundo parcial: "))

    if (parcialUno > 0) & (parcialUno <= 10) & (parcialDos > 0) & (parcialDos <= 10):
        if (parcialUno >= 4) & (parcialDos >= 4):
            print("este alumno aprobo")
            aprobados = aprobados + 1
        elif (parcialUno < 4) & (parcialDos >= 4):
            print("este alumno recupera el primer parcial")
            recuperaPrimero = recuperaPrimero + 1
        elif (parcialUno >= 4) & (parcialDos < 4):
            print("este alumno recupera el segundo parcial")
            recuperaSegundo = recuperaSegundo + 1
        elif (parcialUno < 4) & (parcialDos < 4):
            print("este alumno recupera ambos parciales")
            recuperaAmbos = recuperaAmbos + 1
    else:
        print("las notas ingresadas no son correctas, por favor revise los valores ingresados")
    totalAlumnos = totalAlumnos +1

    legajo = int(input("ingrese el legajo del alumno o 0 para salir: "))

if totalAlumnos > 0:
    print("total Alumnos: ", totalAlumnos)
    print("total aprobados: ", aprobados)
    print("porcentaje aprobados: ", (aprobados/totalAlumnos)*100)
    print("porcentaje recupera primero: ", (recuperaPrimero/totalAlumnos)*100)
    print("porcentaje recupera segundo: ", (recuperaSegundo/totalAlumnos)*100)
    print("porcentaje recupera ambos: ", (recuperaAmbos/totalAlumnos)*100)