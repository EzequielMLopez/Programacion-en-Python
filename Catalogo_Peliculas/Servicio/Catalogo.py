import os

class CatalogoPeliculas():
    ruta_archivo = "peliculas.txt"

    @classmethod
    def agregarpeliculas(cls, pelicula):
        with open(cls.ruta_archivo, "a", encoding="utf8") as archivo:
            archivo.write(f"{pelicula.namepelicula}\n")
    
    @classmethod
    def listarpeliculas(cls):
        with open(cls.ruta_archivo, "r", encoding="utf8") as archivo:
            print("Catalogo de Peliculas".center(50, "-"))
            print(archivo.read())

    @classmethod
    def eliminarpeliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f"Se elimino: {cls.ruta_archivo}")

    
