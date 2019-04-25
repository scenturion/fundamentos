# Generar una serie de 1000 números.
# Informar cuantos números deficientes hay en dicha serie.
# Si el número que está considerando es deficiente, obtener su factorial, para el caso de que el número tenga raíz cuadrada exacta
# Número deficiente: todo número natural n que cumple que la suma de sus divisores propios es menor al número. Ej: 15>1+3+5. El 15 es un número deficiente

i=1
maxrango = 1000
while maxrango >= i:
    
    medio = (i  // 2)
    divisor = 1
    acumuladorDivisores = 0
    while medio >= divisor:
        if i % divisor == 0:
            acumuladorDivisores = acumuladorDivisores + divisor
        divisor = divisor + 1
        
    if (i > acumuladorDivisores) & (acumuladorDivisores > 1):
        print("el numero ", i, "es deficiente")
        raiz = i
        raices = 1
        restaRaices = raiz
        raizCuadrada = -1
        while restaRaices >= 0:
            raiz = restaRaices
            restaRaices = raiz - raices
            raices = raices + 2
            raizCuadrada = raizCuadrada + 1
        if raiz == 0:
            print("el número ", i, " tiene raiz exacta y esta es: ", raizCuadrada)
            restador = i
            factorial = 1
            while restador > 0:
                factorial = factorial * restador
                restador = restador - 1
            print("el factorial del numero antes mencionado es: ", factorial)
    i = i + 1