# Generar una lista con 20 números aleatorios entre el 1 y el 200.

def metodo_seleccion(lista_desordenada):
    lista_aux = lista_desordenada
    for j in range (len(lista_aux) - 1 ):
        for i in range (j + 1, len(lista_aux)):
            if lista_aux[j] > lista_aux[i]:
                aux = lista_aux[i]
                lista_aux[i] = lista_aux[j]
                lista_aux[j] = aux
    return lista_aux
import random
lista_random =[]
divisible = []
cantidad = 20
for i in range(cantidad):
    lista_random.append(random.randint(1,200))
print(lista_random) 
# Generar una segunda lista que almacene los valores de la primera lista que sean múltiplos de 3. 
for i in range(len(lista_random)):
    if (lista_random[i] % 3) == 0:
        divisible.append(lista_random[i])
print(divisible)
# Ordenar la segunda lista con el método de selección (este paso generarlo con una función que tenga valor de retorno)

divisible = metodo_seleccion(divisible)
print(divisible)
# Una vez ordenada la lista tomar el menor valor y validar si es par o impar, sea cual sea la condición informarla con un mensaje.
if (divisible[0] % 2) == 0:
    print("el primer elemento es par: ", divisible[0])
else:
    print("el primer elemento es impar: ", divisible[0])
