#Programa: index18.py
#Proposito: Calcular cual es la menor palabra de 5 que se introduzcan.
#Autor: Ezequiel Lopez
#Fecha: 03/02/2022

def main():

    #Datos de entrada
    pal1 = input("Ingrese una palabra:")
    pal2 = input("Ingrese una palabra:")
    pal3 = input("Ingrese una palabra:")
    pal4 = input("Ingrese una palabra:")
    pal5 = input("Ingrese una palabra:")

    #Operaciones y Salidas
    candidato = pal1
    if(pal2 < candidato):
        candidato = pal2
    if(pal3 < candidato):
        candidato = pal3
    if(pal4 < candidato):
        candidato = pal4
    if(pal5 < candidato):
        candidato = pal5

    print("La menor de las palabras es:", candidato)

main()
