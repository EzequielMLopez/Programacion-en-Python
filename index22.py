#Programa: index22.py
#Proposito: Calificación cualitativa en función de la calificación.
#Autor: Ezequiel Lopez
#Fecha: 05/02/2022

def main():
    #Datos de entrada
    cali = float(input("Ingrese la calificación del alumno:"))

    #Operaciones y Salidas
    if(cali < 5):
        print("Se encuentra SUSPENDIDO")
    elif(cali >= 5 and cali < 7):
        print("Usted es APROBADO")
    elif(cali >= 7 and cali < 8.5):
        print("Usted es NOTABLE")
    elif(cali >= 8.5 and cali < 10):
        print("Usted es SOBRESALIENTE")
    elif(cali == 10):
        print("Usted es MATRICULA DE HONOR")
    else:
        op = int(input("Intentelo más tarde(1)\nVuelva a intentar(2):"))
        if(op == 1):
            print(50*"-")                    
        if(op == 2):
            main()                

main()
