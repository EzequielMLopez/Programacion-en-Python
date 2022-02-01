#Programa: index13.py
#Proposito: Imprimir si la mitad de un numero ingresado es par o impar.
#           Solo valido para enteros pares.
#Autor: Ezequiel Lopez
#Fecha: 01/02/2022

def main():
    #Datos de entrada
    num = int(input("Ingrese un numero:"))
    num = num / 2
    num = (-1) ** num

    #Operaciones
    if(num == -1):
        print("La paridad de la mitad de %d es:impar" % (num))
    elif(num == 1):
        print("La paridad de la mitad de %d es:par" % (num))

main()
