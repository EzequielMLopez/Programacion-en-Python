#Programa: index9.py
#Proposito: Decir si un numero es negativo o positivo.
#Autor: Ezequiel Lopez
#Fecha: 31/01/2022
def main():

    #Valores de entrada
    num = float(input("Ingrese un numero:"))

    #Operaciones
    if(num >= 0):
        print("El numero ingresado es positivo")
    if(num < 0):
        print("El numero ingresado es negativo")

main()
