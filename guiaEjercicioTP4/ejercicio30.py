# Leer un número natural N. Calcular e imprimir los primeros N términos de la sucesión geométrica de razón 3, 
# cuyos primeros términos son 1, 3, 9, 27, 81..... es decir 3^0, 3^1, 3^2, 3^3....

sucesion = int(input("inserte un numero para calcular la potencia de 3 elveado a dicho numero: "))

potencia = 0

valorActual = 1

while potencia <= sucesion:    
    print("para la potencia ", potencia, "de 3 el valor obtenido es: ", valorActual)
    valorActual = valorActual * 3
    potencia = potencia + 1
