#Programa: index25.py
#Proposito: Imprimir en pantalla los multiplos de 6 hasta 150.
#Autor: Ezequiel Lopez
#Fecha: 06/02/2022

def main():
    #Datos de Entrada
    num = 6
    i = 1
    
    #Operaciones y Salidas
    while(i <= 25):
        cont = num * i
        print(cont)
        i+=1

    print("Impresión finalizada")

main()
