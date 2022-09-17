from Monitor import *
from Teclado import *
from Ratón import *

class Computadora:
    cont_pc = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.cont_pc += 1
        self.__cont_pc = Computadora.cont_pc
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    @property
    def nombre(self):
        return self.__nombre

    @property
    def monitor(self):
        return self.__monitor

    @property
    def teclado(self):
        return self.__teclado

    @property
    def raton(self):
        return self.__raton

    @property
    def contpc(self):
        return self.__cont_pc

    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo

    @monitor.setter
    def monitor(self, nuevo):
        self.__monitor = Monitor(input("Marca: "), input("Tamaño: "))

    @teclado.setter
    def teclado(self, nuevo):
        self.__teclado = nuevo

    @raton.setter
    def raton(self, nuevo):
        self.__raton = nuevo

    def __str__(self):
        return (f"""\n
         Nombre: {self.__nombre} ID: {self.__cont_pc}
         {self.__monitor.__str__()}
         {self.__teclado.__str__()}
         {self.__raton.__str__()}""") 



         