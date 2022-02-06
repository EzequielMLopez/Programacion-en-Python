#Programa: index23.py
#Proposito: Calcula el diametro, perimetro o area en función de la opción
#           que escoga el usuario
#Autor: Ezequiel Lopez
#Fecha: 06/02/2022

def main():
    #Importación de librerías
    from math import pi

    #Datos de Entrada
    radio = float(input("Dame el radio de un círculo:"))
    
    print("Escoga una opción:\na)Calcula el diámetro.\n\
b)Calcula el perimetro.\nc)Calcula el área.")
    opc = input("Tecle a, b o c y pulse el retorno de carro:")

    #Operaciones y Salidas
    if(opc == "a" or opc == "A"):
        diam = 2 * radio
        print("El dia es:", diam)
    elif(opc == "b" or opc == "B"):
        peri = 2 * pi * radio
        print("El perímetro es:", peri)
    elif(opc == "c" or opc == "C"):
        area = pi * radio**2
        print("El área es:", area)
    elif:
        print("Las opciones son:a, b, c.")
        print("Usted escogio:", opc)

main()
