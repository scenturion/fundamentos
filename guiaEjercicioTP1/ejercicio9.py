# Un banco necesita para sus cajeros automáticos un programa que lea una cantidad de dinero e imprima a cuántos billetes equivale, 
# considerando que existen billetes de $100, $50, $10, $5 y $1. 
# Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entrega- dos por el cajero.

monto = int(input("inserte el monto que quiere retirar: "))
billetes100, billetes50, billetes10, billetes5, billetes1 = 0, 0, 0, 0, 0

if monto >= 100:
    billetes100 = monto // 100
    monto = monto - (billetes100 * 100)

if monto >= 50:
    billetes50 = monto // 50
    monto = monto - (billetes50 * 50)

if monto >= 10:
    billetes10 = monto // 10
    monto = monto - (billetes10 * 10)

if monto >= 5:
    billetes5 = monto // 5
    monto = monto - (billetes5 * 5)

if monto >= 1:
    billetes1 = monto // 1
    monto = monto - (billetes1 * 1)

print("billetes de 100: ", billetes100)
print("billetes de 50: ", billetes50)
print("billetes de 10: ", billetes10)
print("billetes de 5: ", billetes5)
print("billetes de 1: ", billetes1)