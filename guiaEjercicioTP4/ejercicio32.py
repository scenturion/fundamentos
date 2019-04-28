# La sucesión de Fibonacci es una sucesión de números enteros donde cada término se obtiene como suma de los dos anteriores, 
# siendo los dos primeros 1 y 1. Por lo tanto, Fib=1, 1, 2, 3, 5, 8, 13, 21.... 
# Realizar un programa que lea N e imprima los N primeros términos de esta sucesión, como así también la suma de los mismos.
nMenosDos, nMenosUno = 0, 1
valorEne = int(input("ingrese un valor al que calcularemos la susecion de Fibonacci: "))
serie = 2
if valorEne >= 2:
    while serie <= valorEne:
        fibonacci = nMenosDos + nMenosUno
        nMenosDos = nMenosUno
        nMenosUno = fibonacci
        print("valor n: ", serie, "valor de la serie: ", fibonacci)
        serie = serie + 1
elif valorEne == 0:
    print("valor n: ", 0, "valor de la serie: ", 0)
elif valorEne == 1:
    print("valor n: ", 1, "valor de la serie: ", 1)