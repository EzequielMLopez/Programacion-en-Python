#Programa: index37.py
#Proposito: Semejante al index36 pero la condición se aplica para algunos.
#Autor: Ezequiel Lopez
#Fecha: 15/02/2022

def main():
    #Datos de Entrada
    cad = input("Ingrese una cadena de texto:")
    num = int(input("Ingrese un entero para decir cuantas palabras tienen \
dicha longitud:"))
    creo = False

    #Función encargada de extraer las palabras
    def extraer_palabras(cad, num, creo):
        cad = cad.replace(",", "")
        cad = cad.replace(".", "")
        for p in cad.split():
            if(len(p) == num):
                creo = True
                break
        return creo
    
    #Operaciones y Salidas del main
    creoG = extraer_palabras(cad, num, creo)
    if(creoG):print("EXISTE una palabra que cumple la condición")
    else:print("NO EXISTE palabra que cumple con dicha condición")

main()
