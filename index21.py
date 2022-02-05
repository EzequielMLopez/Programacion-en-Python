#Programa: index20.py
#Proposito: Calcular la cantidad de años en función del capital inicial,
#           capital final y una tasa de interes anual.
#Autor: Ezequiel Lopez
#Fecha: 05/02/2022

def main():
    #Importación de librerías
    from math import log

    #Datos de entrada
    tas = float(input("Ingrese la tasa anual > 0:"))
    cap_ini = float(input("Ingrese el capital inicial:"))
    cap_fin = float(input("Ingrese el capital final:"))

    #Operaciones y Salidas
    if(cap_ini == cap_fin):
        print("La cantidad de años calculados es:0")
    if(tas < 0 or tas == 0):
        tas = int(input("Por favor, que sea un valor de tasa de interes > 0:"))
        if(tas < 0 or tas == 0):
            print("Lo siento papu, vas a tener que empezar de nuevo")
            main()
    if(tas > 0 and cap_ini > 0 and cap_fin > cap_ini): 
        anos = float((abs(log(cap_fin,10)) - abs(log(cap_ini,10))) / abs(log(1 + tas/100,10)))
        print("La cantidad de años es:%0.4f" % (anos))
    if(cap_fin < cap_ini):
        print("Lo que solicita no es posible ejecutar, intentelo más tarde")

main()
