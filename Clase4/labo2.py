#ingresar un nro menor a 50 informar 
# a) si es perfecto: cuando la suma de sus divisores da el numero (por ejemplo el 6)  
# b) abundante: la suma da mas que el nro (ejemplo el 12)  
# c) deficiente: la suma de sus divisores es menor al nro

#obtener los divisores del numero

import random
maxValue = 50
valor = random.randrange(maxValue)
medio = valor // 2
divisor, sumaDivisores = 2, 1
print("se analizara el valor: ", valor)
while divisor <= medio:
    if valor % divisor == 0:
        sumaDivisores = sumaDivisores+divisor
    divisor = divisor + 1

if sumaDivisores == valor:
    print("el numero: ", valor, " es perfecto")
elif sumaDivisores < valor:
    print("el numero: ", valor, "es deficiente, dado que la suma de sus divisores obtenidos es: ", sumaDivisores)
else:
    print("el numero: ", valor, "es abundante, dado que la suma de sus divisores es: ", sumaDivisores)