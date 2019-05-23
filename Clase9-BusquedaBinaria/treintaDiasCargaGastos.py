# completar una lista con 30 valores 0 

diaDelMes = []
mayorGasto = 0

for i in range(0,30):
    diaDelMes.append(0)

dia = 0
# la carga finaliza cuano se ingresa un -1 en la variable dia
while dia != -1: 
    # ingresar el numero de dia y el gasto, 
    dia = int(input("ingrese el dia del gasto (o -1 para salir): "))
    if (dia != -1) & (dia > 0) & (dia < 31):
        gasto = int(input("ingrese el gasto realizado: "))

        # asignar ese importe al dia correspondiente en la lista, puede existir varios importes para un mismo dia, 
        diaDelMes[dia-1] = diaDelMes[dia-1] + gasto

# informar cual fue el dia de mayor gasto y cual fue el gasto
posicion = -1
for i in range(0,30):
    if mayorGasto <= diaDelMes[i]:
        mayorGasto = diaDelMes[i]
        posicion = i

print("el dia de mayor gasto fue el: ", posicion+1)
print("el mayor gasto del mes fue: ", mayorGasto)