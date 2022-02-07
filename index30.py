#Programa: index30.py
#Proposito: Imprimir las combinaciones que podemos formar en función de
#           los datos ingresados por teclado.
#Autor: Ezequiel Lopez
#Fecha: 06/02/2022

def main():
    #Datos de Entrada
    n = int(input("Ingrese la cantidad de elementos de un conjunto;"))
    m = int(input("Ingrese cuantos elementos tomará del conunto:"))
    i = j = k = 1
    fact0 = fact1 = fact2 = 1

    #Operaciones y Salidas
    if(n < m):
        print("Los valores ingresados son ilogicos")

    while(i <= n):
        fact0 *= i
        i += 1
        while(j <= m):
            fact1 *= j
            j += 1
            while(k <= (n - m)):
                fact2 *= k
                k += 1

    print("La cantidad de combinaciones son:%d" % (fact0 / (fact2 . fact1)))

main()
