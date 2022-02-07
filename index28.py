#Programa: index28.py
#Proposito: Imprimir la sumatoria en función de dos numeros ingresados por
#           teclado
#Autor: Ezequiel Lopez
#Fecha: 06/02/2022

def main():
    #Datos de Entrada
    m = int(input("Ingrese el tope de la sumatoria:"))
    n = int(input("Ingrese la base de la sumatoria:"))
    suma = 0

    #Operaciones y Salidas
    if(n > m):
        print("La base debe ser menor que el tope")
        main()
    while(n <= m):
        suma += n
        n += 1
        print(suma)

main()
