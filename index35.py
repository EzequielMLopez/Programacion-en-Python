#Programa: index35.py
#Proposito: Hallar el MCD entre dos numeros ingresados por consola.
#Autor: Ezequiel Lopez
#Fecha: 09/02/2022

def main():
    #Datos de Entrada
    num1 = int(input("Ingrese un valor > 0:"))
    num2 = int(input("Ingrese otro valor > 0 y diferente al primero:"))
    creo = False

    #Operaciones y Salidas
    if(num1 == 0):
        print("Se le solicito un numero mayor que 0, vuelva a empezar")
        main()

    if(num2 == 0 or num2 == num1):
        print("Ingrese lo solicitado, volvera al inicio:")
        main()

    while(creo == False):
        if(num1 == 0):
            print("El MCD entre ambos es:", num2)
            creo = True

        if(num2 == 0):
            print("El MCD entre ambos es:", num1)
            creo = True

        if(num1 > num2):
            if(num2 != 0):
                coc = num1 / num2
                rest = num1 % num2
                num1 = num2
                num2 = rest
            else:
                break

        elif(num1 < num2):
            if(num1 != 0):
                coc = num2 / num1
                rest = num2 % num1
                num2 = num1
                num1 = rest
            else:
                break

main()
