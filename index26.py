#Programa: index26.py
#Proposito: Imprimir los multiplos del primer numero ingresado por teclado
#           hasta la diferencia que se genera con el segundo.
#Autor: Ezequiel Lopez
#Fecha: 06/02/2022

def main():
    #Datos de Entrada
    num1 = float(input("Ingrese un numero:"))
    num2 = float(input("Ingrese un numero mayor al primero:"))
    i = 1

    #Operaciones y Salidas
    if(num1 > num2):
        print("Intentelo de nuevo, cumpliendo las condiciones")
        main()
    div = (num2 - num1) / num1

    while(i <= div):
        cont = num1 * i
        print(cont)
        i += 1

main()

