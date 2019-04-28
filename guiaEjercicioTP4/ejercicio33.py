# La raíz cuadrada de un número positivo n puede calcularse mediante la siguiente fórmula de Newton:
# raiz de n es casi: (n/a + a) / 2
# donde "a" es una aproximación a raiz de n  . 
# Al aplicar repetidamente esta fórmula reemplazando "a" por la aproximación obtenida en el paso anterior, 
# se obtiene cada vez una aproximación mejor. Desarrollar un programa que calcule la raíz cuadrada aproximada de un número entero positivo n, 
# utilizando como primera aproximación a n/2. Detener el proceso cuando la diferencia entre dos cálculos sucesivos sea menor a 0,0001.

aproximacionTolerada = 0.000000000001
entero = int(input("inserte un valor enter positivo para poder calcular su raiz: "))
raizAnterior = entero
raizActual = ((entero / 2) + 2) / 2
if entero >= 0:
    while (raizAnterior - raizActual) > aproximacionTolerada:
        raizAnterior = raizActual
        raizActual = ((entero / raizAnterior) + raizAnterior) / 2
    print("la raiz del valor: ", entero, "es: ", raizActual)
else:
    print("el valor ingresado es negativo, no se puede calcular su raiz")