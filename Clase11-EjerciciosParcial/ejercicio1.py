# Ejercicio 1

# Se ingresa por teclado el nro de legajo de los alumnos de un curso y su nota de examen final.

# El primero se carga en la lista LEGAJOS y el segundo dato, en la lista NOTA_FINAL.

# El fin de la carga se determina ingresando un -1, en la variable del legajo.

# Se debe validar que la nota ingresada sea entre 1 y 10.

# Terminada la carga de datos, recorrer la listas y preparar la siguiente información:

# a – Cantidad de alumnos que aprobaron, nota >=7.

# b – Cantidad de alumnos que rinden examen previo con nota >= 4 y <7

# c – Porcentaje de alumnos que están aplazados. Resolver esto con una función.

# Informar todos los datos obtenidos



# El primero se carga en la lista LEGAJOS y el segundo dato, en la lista NOTA_FINAL.
 
legajos = []
aplazo = 4
nota_final = []

# c – Porcentaje de alumnos que están aplazados. Resolver esto con una función.
# esta funcion recibe una nota que es la que va a usar de condicion
# para poder validar, por ejemplo, notas menores a 7, a 8, o lo que se necesite  
def porcentaje_menor_que(lista, nota_condicion):
    tamanioLista = len(lista)
    cumple_condicion = 0
    for j in range(len(lista)):
        if lista[j] < nota_condicion:
            cumple_condicion = cumple_condicion + 1
    porcentaje = ( cumple_condicion / tamanioLista) * 100
    return porcentaje

# EJERCICIO 2 - Ordenar lista

def ordenar_dos_listas(lista_maestra, lista_hija):
    matriz = []
    band = 1
    while band == 1:
        band = 0
        for i in range(len(lista_maestra)-1):
            if lista_maestra[i] > lista_maestra[i + 1]:
                aux = lista_maestra[i]
                aux_hija = lista_hija[i]
                lista_maestra[i] = lista_maestra[i +1]
                lista_hija[i] = lista_hija[i + 1]
                lista_maestra[i + 1] = aux
                lista_hija[i + 1] = aux_hija
                band = 1
    matriz.append(lista_maestra)
    matriz.append(lista_hija)
    return matriz

# Se ingresa por teclado el nro de legajo de los alumnos de un curso y su nota de examen final.
legajo_actual = int(input("ingrese el legajo del alumno o -1 para salir: "))
while legajo_actual != -1:
    legajos.append(legajo_actual)
    nota_actual = int(input("ingrese la nota del alumno, debe estar comprendida entre 1 y 10: "))
    while (nota_actual > 10 ) or (nota_actual < 1):
        nota_actual = int(input("ingrese la nota del alumno, debe estar comprendida entre 1 y 10: "))
    nota_final.append(nota_actual)
    legajo_actual = int(input("ingrese el legajo del alumno o -1 para salir: "))

aprobaron = 0
previo = 0

for j in range(len(nota_final)):
    if nota_final[j] >= 7:
        aprobaron = aprobaron + 1
    if (nota_final[j] >= 4) and (nota_final[j] <7) :
        previo = previo + 1
# a – Cantidad de alumnos que aprobaron, nota >=7.
print('total mas de 6: ', aprobaron)
# b – Cantidad de alumnos que rinden examen previo con nota >= 4 y <7
print('total a recuperatorio: ', previo)
print('procentaje de aplazados: ', porcentaje_menor_que(nota_final, aplazo))


# Ejercicio 2

# Utilizando las listas anteriores, realizar lo siguiente:

# A – Ordenar la lista LEGAJOS, de manera ascendente, arrastrando la lista NOTA_FINAL.
print(legajos)
matriz_alumno = ordenar_dos_listas(legajos, nota_final)

legajos = matriz_alumno[0]
nota_final = matriz_alumno[1]
# B – Solicitar un legajo por pantalla. Verificar que exista en la lista LEGAJOS. De no existir, solicitarlo nuevamente y volver a realizar la búsqueda.

valorMin= 0
valorMax = len(legajos) - 1
pos = -1
while pos == -1:
    dato = int(input("inserte el lejago del alumno: "))
    while (valorMin <= valorMax) and pos == -1:
        valorMed = (valorMin + valorMax) // 2
        if dato == legajos[valorMed]:
            pos = valorMed
        elif dato > legajos[valorMed]:
            valorMin = valorMed + 1
        else:
            valorMax = valorMed - 1

# C – Informar cual es la nota del alumno ingresado.

print("el alumno con legajo:", legajos[pos], "tiene una nota de:", nota_final[pos])
print(legajos)

