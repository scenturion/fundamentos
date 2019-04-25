# dado un valor a = 0 y un valor b = 1, generar la serie de fibonacci, 
# alias chicho, en donde cada elemento se obtiene por la suma de los dos anteriores
# generar 20 valores

import random

print("FIBONACCI")
a, b, n = 0, 1, 0
i = 2
while i <= 20:
    n = a + b
    a = b
    b = n
    print("en la posocion ", i, "el valor es ", n)
    i = i + 1
# generar de manera aleatoria 1000 valores entre 100 y 900. Informar cuanto es el menor 
# valor que salio y en que posicion salio y cual fue el mayor valor y en que posicion se encontro cada uno
print("EJERCICIO 2")

minimo, maximo = 900, 100
iteracion, minimaPosicion, maximaPosicion = 0, 0, 0

while iteracion < 1000 :
    numero = random.randint(100, 900)
    iteracion = iteracion + 1
    if numero < minimo:
        minimo = numero
        minimaPosicion = iteracion
    elif numero > maximo: 
        maximo = numero
        maximaPosicion = iteracion
print("se recorrieron 10000 posiciones en un rango del 100 al 900, el minimo obtenido es ", minimo, "en la iteracion", minimaPosicion)
print("el maximo obtenido es: ", maximo, "en la posicion: ", maximaPosicion)



# Generar 2 aleatorios el primero entre 100 y 900 el segunddo corresponde a la categoria que va entre 1 y 3 (iterar mil veces). 
# Informar total por categoria, mayor por categoria, total de sueldos y promedio por categoria

maxIteracion = 1000

iteracion = 0
categoria1, categoria2, categoria3 = 1, 2, 3
totalCat1, totalCat2, totalCat3 = 0, 0, 0
mayorCat1, mayorCat2, mayorCat3 = 0, 0, 0
perCat1, perCat2, perCat3 = 0, 0, 0
totalSueldos = 0
while iteracion < maxIteracion:
    categoria = random.randrange(1, 4)
    sueldos = random.randrange(100, 900)
    if categoria == categoria1:
        perCat1 = perCat1 + 1
        totalCat1 = sueldos + totalCat1
        if mayorCat1 < sueldos:
            mayorCat1 = sueldos
    if categoria == categoria2:
        perCat2 = perCat2 + 1
        totalCat2 = sueldos + totalCat2
        if mayorCat2 < sueldos:
            mayorCat2 = sueldos
    if categoria == categoria3:
        perCat3 = perCat3 + 1
        totalCat3 = sueldos + totalCat3
        if mayorCat3 < sueldos:
            mayorCat3 = sueldos
    totalSueldos = sueldos + totalSueldos
    iteracion = iteracion + 1
print("total categoria 1", categoria1, "personas por categoria 1", perCat1," mayor sueldo categoria 1: ", mayorCat1," dinero cat 1: ", totalCat1, totalSueldos)
print("total categoria 2", categoria2, "personas por categoria 2", perCat2," mayor sueldo categoria 2: ", mayorCat2," dinero cat 2: ", totalCat2, totalSueldos)
print("total categoria 3", categoria3, "personas por categoria 3", perCat3," mayor sueldo categoria 3: ", mayorCat3," dinero cat 3: ", totalCat3, totalSueldos)


# Ingresar un valor menor o igual a 100, validar que sea menor o igual a 100. Informar si el valor ingresado tiene raiz cuadrada exacta

# Ingresar un valor menor o igual a 100, informar si el valor ingresado es un nro oblongo. Es un numero producto de dos numeros consecutivos.