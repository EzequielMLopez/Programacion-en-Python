#Programa: index4.py
#Proposito: calcula el radio de un triangulo a partir de dos de sus lados
#           y de su angulo.
#Autor: Ezequiel Lopez
#Fecha: 30/01/2022

def main():
    from math import sin,pi

    a = float(input("Ingrese un lado del triangulo:"))
    b = float(input("Ingrese otro lado del triangulo:"))
    ø = float(input("Ingrese el valor del angulo:"))
    rad = ø * (pi/180) #Lo paso a radianes dado que sin trabaja con radianes
    area = round(((a * b) / 2) * sin(rad),2)

    print ("El area es:",area,"metros cuadrados")
main()
