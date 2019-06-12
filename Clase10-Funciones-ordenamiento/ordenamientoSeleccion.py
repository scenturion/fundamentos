# ordenamiento mediante seleccion

import random
cant = []

for i in range (100):
    cant.append(random.randint(10,30))

# se imprime la lista que se creo
itero = 0
print("lista desordenada: ", cant)

for j in range (len(cant) - 1 ):
    for i in range (j + 1, len(cant)):
        itero = itero + 1
        if cant[j] > cant[i]:
            aux = cant[i]
            cant[i] = cant[j]
            cant[j] = aux
            # imprimo lo que reemplazo
            print("reemplazamos ", aux, "por ",cant[i])

print("lista ordenada: ", cant)
print("vueltas dadas: ", itero)