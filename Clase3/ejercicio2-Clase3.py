#ingresar un nro aleatorio de forma automatica teniendo en cuenta que el numero a ser ingresado debe ser menor o igual a 200, 
# imprimir si es mayor o igual q 50 o menor que 50
#y ademas informar cual fue el nro que el sistema obtuvo.
import random

numero = (random.randrange(200))
condicion = 50
if numero >= condicion:
    print("el numero obtenido (%s) es mayor o igual que " %numero, condicion)
elif numero < condicion:
    print("el numero obtenido (%s) es menor que " %numero, condicion)
print("el numero random obtenido es ", numero)