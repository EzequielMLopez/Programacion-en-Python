#Programa: index8.py
#Proposito: Resolver ecuaciones de grado uno.
#Autor: Ezequiel Lopez
#Fecha: 30/01/2022

def main():

    coe_a = float(input("Ingrese el coeficiente a:"))
    coe_b = float(input("Ingrese el coeficiente b:"))

    if(coe_a == 0):
        print("No hay forma de resolverla")
    if(coe_a != 0):
        x = -coe_b / coe_a
        print("El valor de X es:%0.1f" % (x))

main()
