#Programa: index7.py
#Proposito: Calcula el perimetro y área de una circunferencia.
#Autor: Ezequiel Lopez
#Fecha: 30/01/2022

def main():
    from math import pi

    radio = float(input("Ingrese el radio de la circunferencia:"))
    perimetro = 2 * pi * radio
    area = pi * radio ** 2

    print("El perimetro es:%0.2f metros \nY el radio es:%0.2f metros cuadrados" % (perimetro,area))
main()

