#Programa: index29.py
#Proposito: Imprimir el factorial de un numero positivo ingresado por teclado.
#Autor: Ezequiel Lopez
#Fecha: 06/02/2022

def main():
    #Datos de Entrada
    n = int(input("Ingrese el valor para efectuar su factorial:"))
    i = 1
    fact = 1

    #Operaciones y Salidas
    if(n >= 0):
        while(i <= n):
            fact *= i
            i += 1
            print(fact)
        while(n == 0):
            print(i)
            break
    else:
        print("El numero a ingresar debe ser mayor-igual que cero")
        main()

main()
