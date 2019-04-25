# en una veteriniaria se ingresa el tipo de animal 
# 1) Perro 
# 2) gato 
# 3) conejo. 
# y por cada uno de ellos se ingresa 1 o 2 dependiendo de si es macho o hembra. el fin de ingreso se representa ingresando -1.
# informar la cantidad de animales tratados, cuantas hembras perros y cuantos machos conejos, ingresar de % de gatos tratados

#CONSTANTES
MACHO = 1
HEMBRA = 2
PERRO = 1
GATO = 2
CONEJO = 3
SALIR = -1

# VARIABLES
perroMacho, perroHembra = 0, 0
gatoMacho, gatoHembra = 0, 0
conejoMacho, conejoHembra = 0, 0
total = 0

print("ingrese el tipo de animal: ", PERRO, " para Perro; " , GATO, " para gato; " , CONEJO, " para conejo; o" , SALIR, "para salir ")
tipoAnimal = int(input())

while tipoAnimal != SALIR :
    print("ingrese el sexo del animal: ", MACHO, " para Macho; ", HEMBRA, " para hembra")
    sexoAnimal = int(input())
    if tipoAnimal == PERRO:
        if sexoAnimal == MACHO:
            perroMacho = perroMacho + 1
        elif sexoAnimal == HEMBRA:
            perroHembra = perroHembra + 1
        elif sexoAnimal != MACHO and sexoAnimal != HEMBRA:
            print("ha ingresado un sexo invalido!")
    elif tipoAnimal == GATO:
        if sexoAnimal == MACHO:
            gatoMacho = gatoMacho + 1
        elif sexoAnimal == HEMBRA:
            gatoHembra = gatoHembra + 1
        elif sexoAnimal != MACHO and sexoAnimal != HEMBRA:
            print("ha ingresado un sexo invalido!")
    elif tipoAnimal == CONEJO:
        if sexoAnimal == MACHO:
            conejoMacho = conejoMacho + 1
        elif sexoAnimal == HEMBRA:
            conejoHembra = conejoHembra + 1
        elif sexoAnimal != MACHO and sexoAnimal != HEMBRA:
            print("ha ingresado un sexo invalido!")
    elif tipoAnimal != PERRO and tipoAnimal != GATO and tipoAnimal != CONEJO: 
        print("Ha ingresado un tipo de animal invalido!")
    
    print("ingrese el tipo de animal: ", PERRO, " para Perro; " , GATO, " para gato; " , CONEJO, " para conejo; o" , SALIR, "para salir ")
    tipoAnimal = int(input())

total = perroMacho + perroHembra + gatoHembra + gatoMacho + conejoHembra + conejoMacho
if total != 0 : 
    print("porcentaje de gatos tratados sobre el total: ", ((gatoHembra + gatoMacho)/ total) * 100)
    print("total de animales tratados: ", total)
    print("total perros hembras tratados: ", perroHembra)
    print("total conejos machos: ", conejoMacho)
