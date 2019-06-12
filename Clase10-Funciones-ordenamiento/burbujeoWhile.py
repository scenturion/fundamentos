# ordenamiento de burbuja con for y while
import random
cant= []

for i in range (100):
    cant.append(random.randint(10,12))

band = 1

# se imprime la lista que se creo
itero = 0
print("lista desordenada: ", cant)
while band == 1:
    band = 0
    for i in range(len(cant)-1):
        itero = itero + 1
        if cant[i] > cant[i + 1]:
            aux = cant[i]
            cant[i] = cant[i +1]
            cant[i + 1] = aux
            band = 1
            # se imprime paso a paso
            print("reemplazamos ", aux, "por ",cant[i])
print("lista ordenada: ", cant)
print("vueltas dadas: ", itero)