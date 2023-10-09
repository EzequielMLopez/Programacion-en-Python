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

def stock_martillo(registro):
    with open(registro, "r") as registre:
        next(registre, None)

        for line in registre:
            line= line.rstrip()
            lista= line.split(",")

            if lista[0] == "Martillo":
                print(f"Para el articulo {lista[0]} con código {lista[1]} cuenta con un stock de {lista[3]}")

def mat_art_2930(registro):
    with open(registro, "r") as registre:
        next(registre, None)

        for line in registre:
            line= line.rstrip()
            lista= line.split(",")

            if lista[1] == "2930":
                print(f"El material con que está hecho el artículo con código {lista[1]} es {lista[7]}")

def desc_art(registro):
    with open(registro, "r") as registre:
        next(registre, None)

        for line in registre:
            line= line.rstrip()
            lista= line.split(",")
    
            if lista[0] == "Llave ajustable":
                print(f"Para el articulo {lista[0]} con código {lista[1]} cuenta con un descuento del {lista[8]}%")


registro= r"C:\Users\tetit\OneDrive\Escritorio\Programacion-en-Python\Curso_Alejandro\Desafio_02\registros_ferreteria.csv"
#art_cod_7462(registro)
#art_herramientas(registro)
#stock_martillo(registro)
#mat_art_2930(registro)
desc_art(registro)
