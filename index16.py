#Programa: index16.py
#Proposito: Imprimir si un caracter es una Mayuscuka o en cuyo caso si es una
#           Minuscula o en caso de que no sea una letra dejar constancia.
#Autor: Ezequiel Lopez
#Fecha: 02/02/2022

def main():
    
    #Datos de entrada
    a = ord(input("Ingrese un caracter:"))
    
    #Operaciones y salidas
    if(a >= ord("A") and a <= ord("Z") or a == ord("Ñ")):
        print("El caracter ingresado es una MAYUSCULA")
    if(a >= ord("a") and a <= ord("z") or a == ord("ñ")):
        print("El caracter ingresado es una MINUSCULA")
    elif(a >= ord("0") and a <= ord("9")):
        print("El caracter no es una LETRA")
        
main()
