#Programa: index12.py
#Proposito: Imprimir si un numero es par o impar.
#Autor: Ezequiel Lopez
#Fecha: 31/02/2022

def main():
    
    #Datos de entrada
    num = int(input("Ingrese un numero entero:"))
    dec = (-1) ** num #Variable que almacena la paridad del numero ingresado

    #Operaciones
    if(dec == 1):
        print("El numero ingresado es par")
    elif(dec == -1):
        print("El numero ingresado es impar")

main()
