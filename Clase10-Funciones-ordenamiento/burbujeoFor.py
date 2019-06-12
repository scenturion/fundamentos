# ordenamiento de burbuja con for
import random
cant= []

for i in range (5):
    cant.append(random.randint(10,12))

# se imprime la lista que se creo
itero = 0
print("lista desordenada: ", cant)
for j in range(len(cant)):
    for i in range(len(cant)-1):
        itero = itero + 1
        if cant[i] > cant[i + 1]:
            aux = cant[i]
            cant[i] = cant[i +1]
            cant[i + 1] = aux
            # se imprime paso a paso
            print("reemplazamos ", aux, "por ",cant[i])
print("lista ordenada: ", cant)
print("vueltas dadas: ", itero)