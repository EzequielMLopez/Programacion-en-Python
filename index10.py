#Programa: index10.py
#Proposito: Calcula en base a dos edades quien es más joven o si tienen la
#           misma edad
#Autor: Ezequiel Lopez
#Fecha: 31/01/2022

def main():

    #Datos de entrada
    edad1 = int(input("Ingrese la edad del Usuario1:"))
    edad2 = int(input("Ingrese la edad del Usuario2:"))

    #Operaciones e impresión de resultados
    if edad1 > edad2:
        print("Usuario2 es más joven que Usuario1 por:%d años" % (edad1 - edad2))
    elif(edad1 < edad2):
        print("Usario1 es más joven que Usuario2 por:%d años" % (edad2 - edad1))
    else:
        print("Ambos Usuarios tienen la misma edad")

main()
