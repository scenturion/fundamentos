import random
# escriba una funcion con valor de retorno que al ingresar el año en que nacio, calcule cuantos años tendria este año (2019)
anio_actual = 2019
def edad_actual(anio_nac, anio_vigente):
    return anio_vigente - anio_nac


anio_natalicio = int(input("ingrese el año de nacimiento: "))

print("usted tiene o cumpliria", edad_actual(anio_natalicio, anio_actual), " años")

# ejecute una funcion que pida ingresar un nro como parametro e imprimir los antecesores consecutivos al valor ingresado, a excepción de los que no sean multiplos de 5

def antecesores_divisible_por(divisor):
    valor = random.randrange(900)
    antecesores = []
    print(valor)
    while valor > 1:
        valor = valor - 1
        if (valor % divisor) == 0:
            print("antecesor divisible: ", valor)
            antecesores.append(valor)
    print("los antecesores son: ", antecesores)

antecesores_divisible_por(5)