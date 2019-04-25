# ingresar un numero menor o igual que 100, informar cuantos y cuales son sus divisores, sin el 1 y sin el mismo nro
import random
maxValue = 100
valor = random.randrange(maxValue)
medio = valor // 2
flag, divisoresObtenidos = 2, 0

while flag < medio:
    if valor % flag == 0:
        print("este valor divide al valor obtenido %s" %flag)
        divisoresObtenidos = divisoresObtenidos+1
    flag = flag + 1
        
print("los divisores obtenidos para el %s fueron : " %valor, divisoresObtenidos)
#Arrojar un dado 150 veces, informar cuantas veces salio un as y porcentaje de veces salio un nro par
carasDado = random.randint(1,6)
totalLances, lanceActual=150, 1
ases, pares = 0, 0
while lanceActual <= totalLances:
    print("lance", lanceActual, "valor", carasDado, end=", ")
    if carasDado == 1:
        ases = ases + 1
    elif carasDado % 2 == 0:
        pares = pares + 1
    lanceActual = lanceActual + 1
    carasDado = random.randint(1,6)

print("se obtuvieron ", ases, " ases y los siguientes % de pares: " , (pares/totalLances) * 100 )

# ingresar un valor menor o igual a 100 informar si el valor ingresado es un nro primo
# ingresar un valor menor a 10 obtener su factorial
maxValue = 100
valor = random.randrange(maxValue)
medio = valor // 2
flag, divisoresObtenidos = 2, 0

while flag < medio:
    if valor % flag == 0:
        divisoresObtenidos = divisoresObtenidos+1
    flag = flag + 1
if divisoresObtenidos == 0:
    print("el valor %s es un nro primo" %valor)
else:
    print("el valor obtenido no es primo", valor)

print("FACTORIAL")
maxValue = 10
valor = random.randrange(maxValue)
print("Vamos a obtener el valor del primo de: ", valor)
primo = 1
while valor > 0:
    primo = valor * primo
    valor = valor -1
print("este es el primo: ", primo)

print("Jugamos con el 50")