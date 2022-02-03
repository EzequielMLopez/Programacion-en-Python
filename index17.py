#Programa: index17.py
#Proposito: Determinar el maximo de 5 numeros enteros.
#Autor: Ezequiel Lopez
#Fecha: 03/02/2022

def main():

    #Datos de entrada
    num1 = int(input("Ingrese un numero:"))
    num2 = int(input("Ingrese un numero:"))
    num3 = int(input("Ingrese un numero:"))
    num4 = int(input("Ingrese un numero:"))
    num5 = int(input("Ingrese un numero:"))

    #Operaciones y salidas
    candidato = num1
    if(num2 > candidato):
        candidato = num2
    if(num3 > candidato):
        candidato = num3
    if(num4 > candidato):
        candidato = num4
    if(num5 > candidato):
        candidato = num5

    print("El mayor de todos ellos es:", candidato)

main()






