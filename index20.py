#Programa: index20.py
#Proposito: Calcular el punto más cercano al primero introducido de cinco
#           que se solicitan.
#Autor: Ezequiel Lopez
#Fecha: 03/02/2022

def main():
    #Importación de librerias
    from math import sqrt
    #Datos de entrada
    x0 = int(input("Ingrese un valor para X0:"))
    y0 = int(input("Ingrese un valor para Y0:"))
    x1 = int(input("Ingrese un valor para X1:"))
    y1 = int(input("Ingrese un valor para Y1:"))
    x2 = int(input("Ingrese un valor para X2:"))
    y2 = int(input("Ingrese un valor para Y2:"))
    x3 = int(input("Ingrese un valor para X3:"))
    y3 = int(input("Ingrese un valor para Y3:"))
    x4 = int(input("Ingrese un valor para X4:"))
    y4 = int(input("Ingrese un valor para Y4:"))
    
    #Operaciones y Salidas
    dist = abs(sqrt((x0 - x1)**2 + (y0 - y1)**2))
    candi1 = x1
    candi2 = y1

    if(dist > abs(sqrt((x0 - x2)**2 + (y0 - y2)**2))):
        dist = abs(sqrt((x0 - x2)**2 + (y0 - y2)**2))
        candi1 = x2
        candi2 = y2
    if(dist > abs(sqrt((x0 - x3)**2 + (y0 - y3)**2))):
        dist = abs(sqrt((x0 - x3)**2 + (y0 - y3)**2))
        candi1 = x3
        candi2 = y3
    if(dist > abs(sqrt((x0 - x4)**2 + (y0 - y4)**2))):
        dist = abs(sqrt((x0 - x4)**2 + (y0 - y4)**2))
        candi1 = x4
        candi2 = y4

    print("El punto con menor distancia al primero es:(%d,%d)" \
            % (candi1, candi2))

main()



