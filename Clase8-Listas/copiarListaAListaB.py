# definir dos listas A y B, completar la lista A con 10 valores, una vez completada, 
# copiar los valores de A a B, elemento por elemento

import random
listaA = []
listaB = []
listaC = []
size = 10
valoresPermitidos = 1000

for position in range (size):
    listaA.append(random.randrange(valoresPermitidos))
print("genero la lista A: ", listaA)
# recorro uno a uno el valor de la lista A
for position in range (size):
    listaB.append(listaA[position])

print("copio el valor generado de la lista anterior a la lista B: ",listaB)

# este no es 1 a 1, pero es de asignacion directa:
listaC = listaA

print("se asigna el valor de la lista A a la Lista C: ", listaC)