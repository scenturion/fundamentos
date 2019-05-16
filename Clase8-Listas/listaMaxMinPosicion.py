# cargar una lista con 30 numeros al azar, por fin de proceso informar 
# cuales son y en que posicion estan los valores minimo y maximo de la lista

import random
lista = []
size = 30
valoresPermitidos = 1000
maximoValor = -1
posicionMaximoValor = 0
posicionMinimoValor = 0
minimoValor = valoresPermitidos + 1
cont = 0
for position in range (size):
    lista.append(random.randrange(valoresPermitidos))
    if maximoValor < lista[position]:
        maximoValor=lista[position]
        posicionMaximoValor=position
    if minimoValor > lista[position]:
        minimoValor=lista[position]
        posicionMinimoValor=position

print("maximo valor: ", maximoValor, "se encuentra en la posicion: ", posicionMaximoValor)

print("minimo valor: ", minimoValor, "se encuentra en la posicion: ", posicionMinimoValor)

print(lista)