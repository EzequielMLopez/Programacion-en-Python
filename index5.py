#Programa: index5.py
#Proposito: Calcula la tasa de interes en un intervalo de tiempo.
#Autor: Ezequiel Lopez
#Fecha: 30/01/2022

def main():
    from math import pow

    cant_eur = float(input("Ingrese un valor en euros:"))
    tas_int = 4.5
    cant_años = int(input("Ingrese la cantidad de años:"))
    val_fin = round(cant_eur * pow(1 + tas_int / 100, 20),2)

    print("El monto transcurrido dicho tiempo será:",val_fin)
main()
