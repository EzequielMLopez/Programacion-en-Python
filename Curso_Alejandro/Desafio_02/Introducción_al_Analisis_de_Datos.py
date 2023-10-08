import csv

def art_cod_7462(registro):
    with open(registro, "r") as registre:
        next(registre, None)

        for line in registre:
            line= line.rstrip()
            lista= line.split(",")
            if lista[1] == "7462":
                print(f"El precio del articulo con código 7462 es: {lista[2]}")        

def art_herramientas(registro):
    with open(registro, "r") as registre:
        next(registre, None)
        herramientas= []

        for line in registre:
            line= line.rstrip()
            lista= line.split(",")

            if lista[4] == "Herramientas":
                herramientas.append(lista[0])

    print(f"En la categoría herramientas se cuenta con {len(herramientas)}")    

registro= r"C:\Users\tetit\OneDrive\Escritorio\Programacion-en-Python\Curso_Alejandro\Desafio_02\registros_ferreteria.csv"
art_cod_7462(registro)
art_herramientas(registro)
