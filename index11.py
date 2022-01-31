#Programa: index11.py
#Proposito: Imprimir si un caracter es un parentesis o no lo es.
#Autor: Ezequiel Lopez
#Fecha: 31/01/2022

def main():

    #Datos de entrada
    paren = ord(input("Ingrese un caracter por teclado:"))

    #Operaciones
    if(paren == ord(")") or paren == ord("(")):
        print("Es paréntesis")
    else:
        print("No es un paréntesis")

main()
