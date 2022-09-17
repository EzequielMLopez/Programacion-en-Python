class Peliculas():

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def namepelicula(self):
        return self.__nombre

    @namepelicula.setter
    def namepelicula(self, nuevo):
        self.__nombre = nuevo

    def __str__(self):
        return (f"El objeto contiene la película: {self.__nombre}")