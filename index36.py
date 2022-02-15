#Programa: index36.py
#Proposito: Calcular la cantidad palabras dentro de una cadena que
#           tengan la longitud que el usuario indica
#Autor: Ezequiel Lopez
#Fecha: 15/02/2022

def main():
    #Datos de Entrada
    cad = input("Ingrese una cadena de texto:")
    num = int(input("Ingrese un entero para decir cuantas palabras tienen \
dicha longitud:"))
    
    #Función encargada de extraer las palabras
    def extraer_palabras(cad, num):
        cad = cad.replace(",", "")
        cad = cad.replace(".", "")
        palabras = [p for p in cad.split() if len(p) == num]
        return palabras

    #Salida en función de los datos ingresados y las respectivas operaciones
    print("La cantidad de palabras que cumplen \
con dicha condición son:", len(extraer_palabras(cad, num)))

main()

