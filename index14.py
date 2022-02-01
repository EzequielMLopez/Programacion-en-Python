#Programa: index13.py
#Proposito: Imprimir uno de los 3 mensajes según lo que verifique la condición
#Autor: Ezequiel Lopez
#Fecha: 01/02/2022

def main():

    #Datos de entrada
    num1 = int(input("Ingrese un numero (entero):"))
    num2 = int(input("Ingrese otro numero (entero):"))

    #Operaciones y salidas
    if(num2 == num1**2):
        print("El segundo es el cuadrado exacto del primero")
    elif(num2 > num1**2):
        print("El segundo es mayor al cuadrado del primero")
    else:
        print("El segundo es menor al cuadrado del primero")

main()
            
                
