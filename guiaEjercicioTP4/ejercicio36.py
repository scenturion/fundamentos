# Por cada empleado de una empresa se leen tres datos: 
# N° de legajo, 
# sueldo básico y 
# antigüedad en la empresa. 
# Emitir un listado que informe el número de legajo y el salario de los empleados, calculando el salario de la siguiente forma: 
#   Al sueldo básico se le debe sumar un 5% por año de antigüedad, 
#   agregando un 25% adicional si la misma supera los 10 años. 
# El lote de datos finaliza cuando se ingresa un 0 (cero) como número de legajo.

legajo = int(input("por favor ingrese el nro de legajo del empleado, para finalizar ingrese 0: "))
while legajo != 0 : 
    sueldoBasico = int(input("por favor ingrese el sueldo basico del empleado: "))
    antiguedad = int(input("por favor ingrese la antigüedad del empleado: "))
    #   Al sueldo básico se le debe sumar un 5% por año de antigüedad, 
    salarioCalculado = sueldoBasico + sueldoBasico * ((antiguedad * 5)/ 100)
    #   agregando un 25% adicional si la misma supera los 10 años. 
    if antiguedad > 10:
        salarioCalculado = salarioCalculado * 1.25
    # Emitir un listado que informe el número de legajo y el salario de los empleados
    print("el empleado cuyo legajo es ", legajo, "tiene un salario de : ", salarioCalculado)
    # El lote de datos finaliza cuando se ingresa un 0 (cero) como número de legajo.
    legajo = int(input("por favor ingrese el nro de legajo del empleado, para finalizar ingrese 0: "))