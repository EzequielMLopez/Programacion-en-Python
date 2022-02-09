#Programa: index34.py
#Proposito: Calcular la sumatoria de todos los numeros pares entre los
#           numeros ingresados por consola.
#Autor: Ezequiel Lopez
#Fecha: 09/02/2022

def main():
    #Datos de Entrada
    bas = int(input("Ingrese la base de la sumatoria:"))
    fin = int(input("Ingrese el final de la sumatoria:"))
    suma = 0

    #Operaciones y Salidas
    if((-1)**bas == 1 and (-1)**fin == 1):
        for i in range(bas, fin+1, 2):
            suma += i
        print("La sumatoria(con ambos numeros inclusive por ser pares)",)
        print("es:", suma)

    elif((-1)**bas == -1 and (-1)**fin == 1):
        for i in range(bas+1, fin+1, 2):
            suma += i
        print("La sumatoria(con el ultimo incluido) es:", suma)

    elif((-1)**bas == 1 and (-1)**fin == -1):
        for i in range(bas, fin, 2):
            suma += i
        print("La sumatoria(con el primero incluido) es:", suma)
    
    elif((-1)**bas == -1 and (-1)**fin == -1):
        for i in range(bas+1, fin, 2):
            suma += i
        print("La sumatoria es:", suma)
main()
