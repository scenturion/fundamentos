#Ingresar dos valores A y B (llamar como quieras), obtener y mostrar las 4 operaciones matemáticas: suma resta multiplicacion y division

print("ejercicio en clase")
valor_uno, valor_dos = 0, 0

while not (valor_uno * valor_dos):
    try:
        valor_uno = int(input("inserte un valor por favor: "))
        valor_dos = int(input("inserte un segundo valor por favor: "))

    except ValueError:
        print("te dije que metas valores numericos")

print("suma: ", valor_uno + valor_dos)
print("resta: ", valor_uno - valor_dos)
print("producto: ", valor_uno * valor_dos)
print("cociente: ", valor_uno / valor_dos)