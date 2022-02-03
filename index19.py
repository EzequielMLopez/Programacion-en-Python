#Programa: index19.py
#Proposito: Determinar el numero más cercano al primero ingresado de cinco
#           que se introducen.
#Autor: Ezequiel Lopez
#Fecha: 03/02/2022

def main():
    
    #Importación de librerias
    import math

    #Datos de entrada
    num1 = int(input("Ingrese un numero:"))
    num2 = int(input("Ingrese un numero:"))
    num3 = int(input("Ingrese un numero:"))
    num4 = int(input("Ingrese un numero:"))
    num5 = int(input("Ingrese un numero:"))

    #Operaciones y Salidas
    candi = abs(num1 - num2)
    res = 0

    if(candi > abs(num1 - num3)):
        candi = abs(num1 - num3)
        res = num3
    if(candi > abs(num1 - num4)):
        candi = abs(num1 - num4)
        res = num4
    if(candi > abs(num1 - num5)):
        candi = abs(num1 - num5)
        res = num5

    print("El más cercano al %d es:%d" % (num1, res))

main()
