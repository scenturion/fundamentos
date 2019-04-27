# Se realizó una encuesta entre 100 consumidores. Por cada persona interrogada se ingresan dos valores: 
# El primero indica la aceptación o no del producto A, mediante un 1 (acepta) o un 0 (no acepta). 
# El segundo valor del par corresponde la producto B. Por ejemplo, el par (1,0) señala que el encuestado acepta el producto A pero no el B. 
# Se solicita informar el porcentaje de consumidores que aceptan:
# · El producto A.
# · El producto B.
# · El producto A solamente.
# · El producto B solamente.
# · Ninguno de los dos.
# · Ambos productos.
import random
consumidorActual = 1
consumidores = 100
aceptaA = 0
aceptaB = 0
noAceptaProducto = 0
aceptaAmbos = 0

while consumidorActual <= consumidores:
    aceptaProductoA = random.randrange(0, 2)
    aceptaProductoB = random.randrange(0, 2)
    if (aceptaProductoA == 1) & (aceptaProductoB == 1):
        aceptaAmbos = aceptaAmbos + 1
    if (aceptaProductoA == 1) & (aceptaProductoB == 0):
        aceptaA = aceptaA + 1
    if (aceptaProductoA == 0) & (aceptaProductoB == 1):
        aceptaB = aceptaB + 1
    if (aceptaProductoA == 0) & (aceptaProductoB == 0):
        noAceptaProducto = noAceptaProducto + 1
    consumidorActual = consumidorActual + 1

print("porcentaje de consumidores que acepten el producto A: ", ((aceptaA + aceptaAmbos) * 100) / consumidores)
print("porcentaje de consumidores que acepten el producto B: ", ((aceptaB + aceptaAmbos) * 100) / consumidores)
print("porcentaje de consumidores que acepten unicamente el producto A: ", ((aceptaA ) * 100) / consumidores)
print("porcentaje de consumidores que acepten unicamente el producto B: ", ((aceptaB ) * 100) / consumidores)
print("porcentaje de consumidores que aceptan ambos productos: ", ((aceptaAmbos) * 100) / consumidores)
print("porcentaje de consumidores que no acepta ningun producto: ", ((noAceptaProducto) * 100) / consumidores)