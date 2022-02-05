#Programa: index23.py
#Proposito: Identifica el tipo de caracter ingresado
#Autor: Ezequiel Lopez
#Fecha: 05/02/2022

def main():
    #Datos ingresados
    car = input("Ingrese un caracter:")
    voc = "AEIOU" 
    cons = "BCDFGHJKLMNPQRSTVWXYZ"
    #Operaciones y Salidas
    if(car in voc):
        print("El caracter '%s' es una vocal mayuscula" % (car))
    if(car in cons):
        print("El caracter '%s' es una consonante mayuscula" % (car))
    if(car in voc.lower()):
        print("El caracter '%s' es una vocal miniscula" % (car))
    if(car in cons.lower()):
        print("El caracter '%s' es una consonante minusculas" % (car))
    if(car not in voc and not car in cons and not car in voc.lower()
        and not car in cons.lower()):
        print("Es otro caracter")
main()
