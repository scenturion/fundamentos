# EJERCICIO PARCIAL
# definir dos listas A y B, ya ordenadas de menor a mayor, 
# obtener la lista C que es igual a la union de A y de B 
# C tambien debe quedar ordenad en forma ascendente

listaA = [0,0,0,1,4,7,8,10,16,18,20,22,26,28]
listaB = [1,2,4,5,7,8,9,10,13,15,16,17,18,90]
listaC = []
posicionA = 0
posicionB = 0
longitudA = len(listaA)
longitudB = len(listaB)
while (posicionA < longitudA) & (posicionB < longitudB):
    if listaA[posicionA] < listaB[posicionB]:
        listaC.append(listaA[posicionA])
        posicionA = posicionA + 1
    else:
        listaC.append(listaB[posicionB])
        posicionB = posicionB + 1

while posicionB < longitudB:
        listaC.append(listaB[posicionB])
        posicionB = posicionB + 1
while posicionA < longitudA:
        listaC.append(listaA[posicionA])
        posicionA = posicionA + 1
print(listaC)