#ingresar un nro  par que sera el limite de una secuencia, con el ciclo while imprima todos los nros menores a dicho limite, los cuales tmbn deben ser pares. 
esMenor = 0
condicion = 1
while (condicion % 2) == 1:
    condicion = int(input("ingrese numero par: "))
while esMenor < condicion:
    print("este numero es menor y es par : ", esMenor)
    esMenor = esMenor + 2
