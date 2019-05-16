# Ejmeplos
# lista de frutas
frutas = ['manzana','banana','pera']
# cantidades
cantidades = [1,2,3,4]
# matrices
matriz = [[1,2,3],[4,5,6],[7,8,9]]

# las listas se populan cuando se inicializa o desde el teclado, una lista vacia es la siguiente:
miLista = []

# metimos el for como ciclo, va a iterar hasta que alcance el valor de cant
# y mientras tanto, populo los elementos de la lista
cant = int(input("ingrese cantidad de elementos de la lista: "))

for i in range (cant):
    elemento = input("elemento? ")
    miLista.append(elemento)
    # imprimo el valor de i, solo para mostrar que i empieza en 0 y termina en cantidad-1
    print(i)
# imprimo los elementos de la lista
print(miLista)