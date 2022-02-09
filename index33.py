#Programa: index33.py
#Proposito: Calcular la raiz n-esima de un valor ingresado por teclado.
#Autor: Ezequiel Lopez
#Fecha: 09/02/2022

def main():
    #Datos de Entrada
    num = float(input("Digite un numero:"))

    #Operaciones y Salidas
    for n in range(2,101):
        print("%f-esima de %f es:%f" % (num, n, num**(1.0/n)))

main()
