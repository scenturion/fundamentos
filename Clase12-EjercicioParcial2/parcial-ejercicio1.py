# Generar una función que al ser llamada reciba como parámetro un número ingresado por teclado. 
# La función debe calcular e imprimir la factorial del número ingresado.

def factorial(factor):
    resultado = 1
    for i in range(factor):
        i = i+1
        resultado = resultado * i
    return resultado

valor = int(input("ingrese un nro para calcular su factorial: "))
print("el factorial de", valor, "es:", factorial(valor))
