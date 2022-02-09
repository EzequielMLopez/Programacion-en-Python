#Programa: index32.py
#Proposito: Desglosar el valor ingresado en euros en los diversos billetes
#           y monedas que hay.
#Autor: Ezequiel Lopez
#Fecha: 09/02/2022

def main():
    #Datos de Entrada
    num = int(input("Ingrese un valor en euros:"))
    
    #Operaciones y Salidas
    for Div in [500, 200, 100, 50, 20, 10, 5]:
        coc = num / Div 
        num = num % Div
        print("%d billetes de %d" % (coc, Div))
    
    for Div in [2, 1]:
        coc = num / Div
        num = num % Div
        print("%d monedas de %d" % (coc, Div))

main()
