#Programa: index38.py
#Proposito: Semejante al index36 pero la condición se aplica para todos.
#Autor: Ezequiel Lopez
#Fecha: 15/02/2022

def main():
    #Datos de Entrada
    cad = input("Ingrese una cadena de texto:")
    num = int(input("Ingrese un entero para decir cuantas palabras tienen \
dicha longitud:"))
    creo = True

    #Función encargada de extraer las palabras
    def extraer_palabras(cad, num, creo):
        cad = cad.replace(",", "")
        cad = cad.replace(".", "")
        for p in cad.split():
            if not(len(p) == num):
                creo = False
                break
        return creo
    
    #Operaciones y Salidas del main
    creoG = extraer_palabras(cad, num, creo)
    if(creoG):print("La condición se cumple para TODOS")
    else:print("La condición no se cumple para TODOS")

main()
