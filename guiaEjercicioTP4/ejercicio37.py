# Una empresa cuenta con 100 empleados, divididos en tres categorías A, B y C. Por cada empleado se lee su legajo, categoría y salario. 
# Se solicita elaborar un informe que contenga:
# · Importe total de salarios pagados por la empresa.
# · Cantidad de empleados que ganan más de $20000.
# · Cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”.
# · Legajo del empleado que más gana.
# · Sueldo más bajo.
# · Importe total de sueldos por cada categoría.
# · Salario promedio.

import random
cantidadEmpleados = 100
legajoNro = 1
maxSueldo = 30000
minSueldo = 1500

totalSalariosPagados = 0
empleadosGananMasDe = 0
empleadosGananMenosDe = 0
legaoEmpleadoMasGana = 0
sueldoMasBajo = maxSueldo
sueldoMasAlto = minSueldo
sueldoTotalCatA = 0
sueldoTotalCatB = 0
sueldoTotalCatC = 0
salarioPromedio = 0

while legajoNro <= cantidadEmpleados:
    categoria = random.randrange(1,4)
    salario = random.randrange(minSueldo, maxSueldo)
    # Importe total de salarios pagados por la empresa.
    totalSalariosPagados = totalSalariosPagados + salario
    # Cantidad de empleados que ganan más de $20000.
    if salario > 20000:
        empleadosGananMasDe = empleadosGananMasDe + 1
    # · Legajo del empleado que más gana.
    if salario > sueldoMasAlto:
        sueldoMasAlto = salario
        legaoEmpleadoMasGana = legajoNro
    # · Sueldo más bajo.
    if sueldoMasBajo > salario:
        sueldoMasBajo = salario

    # · Importe total de sueldos por cada categoría.
    if categoria == 1:
        sueldoTotalCatA = salario + sueldoTotalCatA
    elif categoria == 2:
        sueldoTotalCatB = salario + sueldoTotalCatB
    elif categoria == 3:
        sueldoTotalCatC = salario + sueldoTotalCatC
        # · Cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”.
        if salario < 5000:
            empleadosGananMenosDe = empleadosGananMenosDe + 1
    legajoNro = legajoNro + 1

print("Importe total de salarios pagados por la empresa :", totalSalariosPagados)
print("Cantidad de empleados que ganan más de $20000: ", empleadosGananMasDe)
print("Cantidad de empleados que ganan menos de $5000, cuya categoría sea C", empleadosGananMenosDe)
print("Legajo del empleado que más gana: ", legaoEmpleadoMasGana, sueldoMasAlto)
print("Sueldo más bajo: ", sueldoMasBajo)
print("Importe total de sueldos por categoría A: ", sueldoTotalCatA)
print("Importe total de sueldos por categoría B: ", sueldoTotalCatB)
print("Importe total de sueldos por categoría C: ", sueldoTotalCatC)
# · Salario promedio.
print("Salario promedio: ", totalSalariosPagados/cantidadEmpleados)
