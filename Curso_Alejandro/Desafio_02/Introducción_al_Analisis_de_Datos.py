import csv

def art_cod_7462(registro):
    with open(registro) as registre:
        print(registre.read())
        #next(registre, None)
        #for line in registre:
        #    line= line.rstrip()
        #    lista= line.split(",")
        #    nombre= lista[0]
        #    print(nombre)



registro= r"C:\Users\tetit\OneDrive\Escritorio\Programacion-en-Python\Curso_Alejandro\Desafio_02\registros_ferreteria.csv"
art_cod_7462(registro)
