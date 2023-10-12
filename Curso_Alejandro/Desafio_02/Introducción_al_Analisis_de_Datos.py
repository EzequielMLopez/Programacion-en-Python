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

def prov_caro(registro):
    with open(registro, "r") as registre:
        next(registre, None)
    
        for line in registre:
            line= line.rstrip()
            lista= line.split(",")

            if float(lista[2]) > 0:
                caro= float(lista[2])
                proovedor= lista[5]
            
    print(f"El proveedor del artículo más caro es {proovedor} con un precio de {caro}")

def peso_art_cod(registro):
    with open(registro, "r") as registre:
        next(registre, None)
    
        for line in registre:
            line= line.rstrip()
            lista= line.split(",")

            if float(lista[1] == "5273"):
                print(f"El peso del articulo {lista[0]} con código {lista[1]} es de {lista[6]}kg")

def cat_art_vend(registro):
    mas_vendido= 0
    categoria= ""
    with open(registro, "r") as registre:
        next(registre, None)
    
        for line in registre:
            line= line.rstrip()
            lista= line.split(",")

            if int(lista[9]) > mas_vendido:
                mas_vendido= lista[9]
                categoria= lista[4]
                
    print(f"La categoría del artículo más vendido, hablando de un total de {mas_vendido} por mes es {categoria}")

def nom_art_bajo(registro):
    mas_bajo= 9999999999
    nombre_articulo= ""
    with open(registro, "r") as registre:
        next(registre, None)
    
        for line in registre:
            line= line.rstrip()
            lista= line.split(",")

            if int(lista[2]) < mas_bajo:
                nombre_articulo= lista[0]
    
    print(f"Se encontro el producto {nombre_articulo} con el precio más bajo")

        
registro_window= r"C:\Users\tetit\OneDrive\Escritorio\Programacion-en-Python\Curso_Alejandro\Desafio_02\registros_ferreteria.csv"
registro_linux= r"/home/eml/Escritorio/Programacion-en-Python/Curso_Alejandro/Desafio_02/registros_ferreteria.csv"
#art_cod_7462(registro)
#art_herramientas(registro)
#stock_martillo(registro)
#mat_art_2930(registro)
#desc_art(registro)
#prov_caro(registro_linux)
#peso_art_cod(registro_linux)
#cat_art_vend(registro_linux) # EN EL .CSV FALTAN LAS VENTAS MENSUALES
#nom_art_bajo(registro_linux)

