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

def cant_total_art_stock(registro):
    art_stock= 0
    with open(registro, "r") as registre:
        next(registre, None)
    
        for line in registre:
            line= line.rstrip()
            lista= line.split(",")

            art_stock += int(lista[3])
            
    print(f"La cantidad total de artículos en stock es de {art_stock}")

def prom_pre_art(registro):
    contadorA= 0
    contadorB= 0
    contadorC= 0
    contadorD= 0
    contadorE= 0
    contadorF= 0
    contadorG= 0
    contadorH= 0
    contadorI= 0
    contadorJ= 0
    contadorK= 0
    contadorL= 0
    contadorM= 0
    contadorN= 0
    contadorO= 0
    contadorP= 0
    contadorQ= 0
    contadorR= 0
    contadorS= 0
    contadorT= 0

    sumadorA= 0
    sumadorB= 0
    sumadorC= 0
    sumadorD= 0
    sumadorE= 0
    sumadorF= 0
    sumadorG= 0
    sumadorH= 0
    sumadorI= 0
    sumadorJ= 0
    sumadorK= 0
    sumadorL= 0
    sumadorM= 0
    sumadorN= 0
    sumadorO= 0
    sumadorP= 0
    sumadorQ= 0
    sumadorR= 0
    sumadorS= 0
    sumadorT= 0
    
    with open(registro, "r") as registre:
        next(registre, None)
    
        for line in registre:
            line= line.rstrip()
            lista= line.split(",")

            if lista[0] == "Clavos":   
                sumadorA += float(lista[2])
                contadorA += 1
            elif lista[0] == "Tornillos":
                sumadorB += float(lista[2])
                contadorB += 1
            elif lista[0] == "Herramienta multiusos":
                sumadorC += float(lista[2])
                contadorC += 1
            elif lista[0] == "Brocas":
                sumadorD += float(lista[2])
                contadorD += 1
            elif lista[0] == "Cerradura":
                sumadorE += float(lista[2])
                contadorE += 1
            elif lista[0] == "Pala":
                sumadorF += float(lista[2])
                contadorF += 1
            elif lista[0] == "Taladro":
                sumadorG += float(lista[2])
                contadorG += 1
            elif lista[0] == "Pintura":
                sumadorH += float(lista[2])
                contadorH += 1
            elif lista[0] == "Candado":
                sumadorI += float(lista[2])
                contadorI += 1
            elif lista[0] == "Tornillo de banco":
                sumadorJ += float(lista[2])
                contadorJ += 1
            elif lista[0] == "Martillo":
                sumadorK += float(lista[2])
                contadorK += 1
            elif lista[0] == "Destornillador":
                sumadorL += float(lista[2])
                contadorL += 1
            elif lista[0] == "Lampara":
                sumadorM += float(lista[2])
                contadorM += 1
            elif lista[0] == "Alicates":
                sumadorN += float(lista[2])
                contadorN += 1
            elif lista[0] == "Sierra":
                sumadorO += float(lista[2])
                contadorO += 1
            elif lista[0] == "Llave ajustable":
                sumadorP += float(lista[2])
                contadorP += 1
            elif lista[0] == "Llave de tubo":
                sumadorQ += float(lista[2])
                contadorQ += 1
            elif lista[0] == "Cinta metrica":
                sumadorR += float(lista[2])
                contadorR += 1
            elif lista[0] == "Cepillo":
                sumadorS += float(lista[2])
                contadorS += 1
            elif lista[0] == "Cables electricos":
                sumadorT += float(lista[2])
                contadorT += 1
                
    print(f"""El promedio de precios para el producto "Clavos" es: {sumadorA / contadorA:.2f}
              En el caso del producto "Tornillos" es : {sumadorB / contadorB:.2f}
              En el caso del producto "Herramientas multiusos" es: {sumadorC / contadorC:.2f}
              En el caso del producto "Brocas" es: {sumadorD / contadorD:.2f})
              En el caso del producto "Cerradura" es: {sumadorE / contadorE:.2f}
              En el caso del producto "Pala" es: {sumadorF / contadorF:.2f}
              En el caso del producto "Taladro" es: {sumadorG / contadorG:.2f}
              En el caso del producto "Pintura" es: {sumadorH / contadorH:.2f}
              En el caso del producto "Candado" es: {sumadorI / contadorI:.2f}
              En el caso del producto "Tronillo de banco" es: {sumadorJ / contadorJ:.2f}
              En el caso del producto "Martillo" es: {sumadorK / contadorK:.2f}
              En el caso del producto "Destornillador" es: {sumadorL / contadorL:.2f}
              En el caso del producto "Lampara" es: {sumadorM / contadorM:.2f}
              En el caso del producto "Alicates" es: {sumadorN / contadorN:.2f}
              En el caso del producto "Sierra" es: {sumadorO / contadorO:.2f}
              En el caso del producto "Llave ajustable" es: {sumadorP / contadorP:.2f}
              En el caso del producto "Llave de tube" es: {sumadorQ / contadorQ:.2f}
              En el caso del producto "Cinta metrica" es: {sumadorR / contadorR:.2f}
              En el caso del producto "Cepillo" es: {sumadorS / contadorS:.2f}
              En el caso del producto "Cables electricos" es: {sumadorT / contadorT:.2f}""")
        
def art_caro(registro):
    with open(registro, "r") as registre:
        next(registre, None)
    
        for line in registre:
            line= line.rstrip()
            lista= line.split(",")

            if float(lista[2]) > 0:
                caro= lista[0]
                proveedor= lista[5]
            
    print(f"El artículo más caro de la ferretería es \"{caro}\" cuyo proveedor es {proveedor}")
    
def art_men_ven(registro):
    with open(registro, "r") as registre:
        next(registre, None)
    
        for line in registre:
            line= line.rstrip()
            lista= line.split(",")
            
def prom_stock_cat(registro):
    contadorA= 0
    contadorB= 0
    contadorC= 0
    contadorD= 0
    contadorE= 0

    sumadorA= 0
    sumadorB= 0
    sumadorC= 0
    sumadorD= 0
    sumadorE= 0
    
    with open(registro, "r") as registre:
        next(registre, None)
    
        for line in registre:
            line= line.rstrip()
            lista= line.split(",")
            
            if lista[4] == "Electricidad":
                contadorA += 1
                sumadorA += int(lista[3])
            elif lista[4] == "Ferreteria":
                contadorB += 1
                sumadorB += int(lista[3])
            elif lista[4] == "Pintura":
                contadorC += 1
                sumadorC += int(lista[3])
            elif lista[4] == "Plomeria":
                contadorD += 1
                sumadorD += int(lista[3])
            elif lista[4] == "Herramientas":
                contadorE += 1
                sumadorE += int(lista[3])

    print(f"""El promedio en stock para la categoría "Electricidad" es: {sumadorA / contadorA:.2f}
En el caso de la categoría "Ferreteria" es : {sumadorB / contadorB:.2f}
En el caso del producto "Herramientas multiusos" es: {sumadorC / contadorC:.2f}
En el caso del producto "Brocas" es: {sumadorD / contadorD:.2f}
En el caso del producto "Cerradura" es: {sumadorE / contadorE:.2f}""")

def prom_des(registro):
    sumador= 0
    contador= 0
    
    with open(registro, "r") as registre:
        next(registre, None)
    
        for line in registre:
            line= line.rstrip()
            lista= line.split(",")
            
            sumador += float(lista[8])
            contador += 1
    
    print(f"El descuento promedio en porcentaje es de {(sumador / contador)}%")
    



registro_window= r"C:\Users\tetit\OneDrive\Escritorio\Programacion-en-Python\Curso_Alejandro\Desafio_02\registros_ferreteria.csv"
registro_linux= r"/home/eml/Escritorio/Programacion-en-Python/Curso_Alejandro/Desafio_02/registros_ferreteria.csv"

# PREGUNTAS SOBRE ARTÍCULOS DE LA FERRETERÍA
#art_cod_7462(registro)
#art_herramientas(registro)
#stock_martillo(registro)
#mat_art_2930(registro)
#desc_art(registro)
#prov_caro(registro_linux)
#peso_art_cod(registro_linux)
#cat_art_vend(registro_linux) # EN EL .CSV FALTAN LAS VENTAS MENSUALES
#nom_art_bajo(registro_linux)
#cant_total_art_stock(registro_linux)

# PREGUNTAS ESTADÍSTICAS
#prom_pre_art(registro_linux)
#total_ventas_mensuales(registro_linux) # EN EL .CSV FALTAN LAS VENTAS MENSUALES
#art_caro(registro_linux)
#art_men_ven(registro_linux) # EN EL .CSV FALTAN LAS VENTAS MENSUALES
#prom_stock_cat(registro_linux)
#prom_des(registro_linux)


