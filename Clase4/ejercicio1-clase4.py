#while 
import random
rangeRandom = 3
numero = (random.randrange(rangeRandom))
condicion = int(input("ingrese una condicion de valor: "))
intentos = 0
# si la condicion es mayor al rango, nunca vamos a terminar el loop
if rangeRandom > condicion:
    while condicion > numero:
        print("el numero obtenido es (%s) que es menor que " %numero, condicion)
        print("vamos a obtener otro valor random para salir del while")
        numero = (random.randrange(rangeRandom))
        intentos = intentos + 1
    print("el numero random obtenido es %s" %numero)
    print("el numero de comparaciones fue de %s" %intentos)
else:
    print("si entramos por ahi, es un loop infinito")

