# generar los 20 primeros valores de la sucesion de fibonacci 
# y cargarlos en una lista, 


print("FIBONACCI")
listaFibo = [0, 1]

for i in range(2,20):
    listaFibo.append(listaFibo[i-1]+listaFibo[i-2])

# ingresar un valor

dato = int(input("inserte un valor a buscar en la lista: "))

# informar si se encuentra en la lista y en que pos se encuentra 

valorMin= 0
valorMax = len(listaFibo) - 1
pos = -1

while (valorMin <= valorMax) and pos == -1:
    valorMed = (valorMin + valorMax) // 2
    if dato == listaFibo[valorMed]:
        pos = valorMed
    elif dato > listaFibo[valorMed]:
        valorMin = valorMed + 1
    else:
        valorMax = valorMed - 1

if pos != -1:
    print("esta el valor buscado esta en la posicion:", pos,"de la lista")
else:
    print("no se encontro el valor")