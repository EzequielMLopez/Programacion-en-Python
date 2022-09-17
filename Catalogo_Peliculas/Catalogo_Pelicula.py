#Programa: Catalogo_Peliculas.py
#Proposito: Simular la gestión de un catalogo de películas.
#Autor: Ezequiel Lopez
#Fecha: 15/08/2022

from Dominio.Peliculas import Peliculas
from Servicio.Catalogo import CatalogoPeliculas

if __name__ == "__main__":

    veracidad = None
    while(veracidad != 4):
        try:
            print("""
            1- Agregar_Pelicula
            2- Listar_Pelicula
            3- Eliminar Archivo de Pelicula
            4- Salir""")
            veracidad = int(input("Ingrese la opción deseada: "))

            if(veracidad == 1):
                nombre_pelicula = input("Proporciona el nombre de la pelicula: ")
                pelicula = Peliculas(nombre_pelicula)
                CatalogoPeliculas.agregarpeliculas(pelicula)
            elif(veracidad == 2):
                CatalogoPeliculas.listarpeliculas()
            elif(veracidad == 3):
                CatalogoPeliculas.eliminarpeliculas()

        except Exception as e:
            print(f"Ocurrio un error: {e}")
            veracidad = None

    else:
       print("Hasta la proximaaaa :)") 
        