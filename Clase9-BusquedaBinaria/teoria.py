# busqueda binaria es una busqueda realizada en una lista ordenada
# ejemplo: 
listaOrdenada = [3, 5, 10, 15, 22, 34, 48, 60]
# buscar en al lista 15 si es que aparece
valorMin= 0
valorMax = len(listaOrdenada) - 1
pos = -1
dato = int(input("inserte un valor a buscar en la lista: "))
while (valorMin <= valorMax) and pos == -1:
    valorMed = (valorMin + valorMax) // 2
    if dato == listaOrdenada[valorMed]:
        pos = valorMed
    elif dato > listaOrdenada[valorMed]:
        valorMin = valorMed + 1
    else:
        valorMax = valorMed - 1

if pos != -1:
    print("esta el valor buscado esta en la posicion:", pos,"de la lista")
else:
    print("no se encontro el valor")
