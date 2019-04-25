print("vamos a empezar a programar en python")
valor_uno, valor_dos = 0, 0
while not (valor_uno * valor_dos):
    try:
        valor_uno = int(input("inserte un valor por favor: "))

    except ValueError:
        print("te dije que metas valores numericos")

    try:
        valor_dos = int(input("inserte un segundo valor por favor: "))

    except ValueError:
        print("te dije que metas valores numericos")

print("aca tenemos la suma: ", valor_uno + valor_dos)
print("aca tenemos la resta: ", valor_uno - valor_dos)
