#Programa: index31.py
#Proposito: Accionar acorde a la opcion que elije el usuario por teclado.
#Autor: Ezequiel Lopez
#Fecha: 07/02/2022
#Info: La opción 8 no la puedo ejecutar por errores, buscar forma de sol.

def main():
    #Importar Librerias
    from math import sqrt, acos, pi

    #Datos Base
    opc = 1
    print(180/pi)

    #Menu
    while(opc >= 1 and opc < 9):
        print("1) Introducir el vector1")
        print("2) Introducir el vector2")
        print("3) Calcular la suma")
        print("4) Calcular la diferencia")
        print("5) Calcular el producto escalar")
        print("6) Calcular el producto vectorial")
        print("7) Calcular el angulo (en grados) entre ellos")
        print("8) Calcular la longitud")
        print("9) Finalizar")
        opc = int(input())

    #Operaciones y Salidas
        if(opc == 1):
            x1 = float(input("Ingrese el valor de x del Vector1:"))
            y1 = float(input("Ingrese el valor de y del Vector1:"))
            z1 = float(input("Ingrese el valor de z del Vector1:"))

        if(opc == 2):
            x2 = float(input("Ingrese el valor de x del Vector2:"))
            y2 = float(input("Ingrese el valor de y del Vector2:"))
            z2 = float(input("Ingrese el valor de z del Vector2:"))

        if(opc == 3):
            print("La Suma es:(%0.2f,%0.2f,%0.2f)" % (x1+x2,y1+y2,z1+z2))
        
        if(opc == 4):
            opc1 = 0
            while(opc1 < 1 or opc1 > 2):
                print("1) Se efectua Vector1 menos Vector2")
                print("2) Se efectua Vector2 menos Vector1")
                opc1 = int(input())
            if(opc1 == 1):
                print("La Resta del Vector1 menos Vector2 es:\
(%0.2f,%0.2f,%0.2f)" % (x1-x2, y1-y2, z1-z2))
            elif(opc1 == 2):
                print("La Resta del Vector2 menos Vector1 es:\
(%0.2f,%0.2f,%0.2f)" % (x2-x1, y2-y1, z2-z1))

        if(opc == 5):
            print("El Producto Escalar es:%0.2f" % ((x1*x2)+(y1*y2)*(z1*z2)))
            
        if(opc == 6):
            opc2 = 0
            while(opc2 < 1 or opc2 > 2):
                print("1) Producto vectorial del Vector1 con Vector2")
                print("2) Producto vectorial del Vector2 con Vector1")
                opc2 = int(input())
            if(opc2 == 1):
                print("El Producto Vectorial del Vector1 con Vector2 es:\
(%0.2f, %0.2f, %0.2f)" % (y1*z2-z1*y2,z1*x2-x1*z2,x1*y2-y1*x2))
            elif(opc2 == 2):
                print("El Producto Vectorial del Vector2 con Vector1 es:\
(%0.2f, %0.2f, %0.2f)" % (y2*z1-z2*y1,z2*x1-x2*z1,x2*y1-y2*x1))

        if(opc == 7):
            if((x1+y1+z1) == 0 or (x2+y2+z2) == 0):
                print("No se puede efectuar división por cero,\
                        consecuentemente el angulo no existe")
            
            normas1 = sqrt((x1)**2 + (y1)**2 + (z1)**2)
            normas2 = sqrt((x2)**2 + (y2)**2 + (z2)**2)
            prod_punt = (x1*x2)+(y1*y2)*(z1*z2)
            print("El Angulo(grados) es:%0.2f" % 
                    (acos(prod_punt / (normas1 * normas2))))
        
        if(opc == 8):
            opc3 = 0
            while(opc3 < 1 or opc3 > 2):
                print("1) Se efectua la longitud del Vector1")
                print("2) Se efectua la longitud del Vector2")
                opc3 = int(input())
            if(opc3 == 1):
                print("La Longitud del Vector1 es:%0.2f" % (normas1)) 
            elif(opc3 == 2):
                print("La Longitud del Vector2 es:%0.2f" % (normas2))
         
    print("Gracias por usar el programa")

main()
