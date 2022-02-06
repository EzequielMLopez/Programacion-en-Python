#Programa: index27.py
#Proposito: Imprimir todas las potencias de 2 hasta 2**30.
#Autor: Ezequiel Lopez
#Fecha: 06/02/2022

def main():
    #Datos de Entrada
    num = 2
    i = 0

    #Operaciones y Salidas
    while(i <= 30):
        cont = num ** i
        print(cont)
        i += 1

main()
