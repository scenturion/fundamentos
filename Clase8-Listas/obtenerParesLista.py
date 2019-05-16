# cargar una lista con 20 valores, luego de generada indicar cuantos valores pares hay en la lista

import random
lista = []
size = 20
valoresPermitidos = 100
cont = 0
for position in range (size):
    lista.append(random.randrange(valoresPermitidos))

print(lista)

for position in range (size):
    if lista[position] % 2 == 0:
        print("este valor de la lista es par: ", lista[position], "y esta es la posicion: ", position)
        cont = cont + 1

print("cantidad de valores pares: ", cont)
