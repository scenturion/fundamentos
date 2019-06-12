
# FUNCION sin parametros
def muestra_numeros():
    print(1, 2, 3)

# funcion con parametros
def muestra_numeros_con_parametros(a, b, c):
    print(a, b, c)

# retornando valores
def area_rombo(diagonal1, diagonal2):
    area = diagonal1 * diagonal2 / 2
    return area

def cambio(fruta):
    valor = fruta + 67
    print("el valor ingresado se cambio a: ", valor)
    return valor

muestra_numeros()

muestra_numeros_con_parametros("hola", "mundo", "!!")

muestra_numeros()

valor_de_area = area_rombo(5, 8)

print("el area del rombo es: ", valor_de_area)

print("el area del rombo es: ", area_rombo(4, 3))

# la variable la puedo declara despues de declarada la funcion (la declaré en la linea 15), pero no antes de llamar a la funcion (la llamo en la linea 36)
variable = 5

print(variable)
variable = cambio(variable)
print(variable)
variable = cambio(variable)
print(variable)