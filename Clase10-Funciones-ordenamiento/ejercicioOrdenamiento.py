# crear 2 listas, donde la primera registra las surcursales A B C D y E
# en la segunda lista ingresar los importes diarios A = 37500, B = 48200, C = 47300, D = 47800, E = 31400
# con el metodo de ordenamiento de burbuja ordene los importes en forma ascendente, al finalizar imprimir las dos listas 
# para visializar cual fue la sucursal que menos vendio y la que mas vendio

def matriz_desordenada(matriz_vieja):
    band = 1
    while band == 1:
        band = 0
        for i in range(len(matriz_vieja[1])-1):
            if matriz_vieja[1][i] > matriz_vieja[1][i + 1]:
                aux = matriz_vieja[1][i]
                aux2 = matriz_vieja[0][i]
                matriz_vieja[1][i] = matriz_vieja[1][i +1]
                matriz_vieja[0][i] = matriz_vieja[0][i + 1]
                matriz_vieja[1][i + 1] = aux
                matriz_vieja[0][i + 1] = aux2
                band = 1
    return matriz_vieja

matriz = [["A","B","C","D","E"],[37500,48200,47300,47800,31400]]
itero = 0
print("lista desordenada: ", matriz)


print(matriz_desordenada(matriz))