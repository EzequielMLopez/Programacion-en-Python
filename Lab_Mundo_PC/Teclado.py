from DispositivoEntrada import *

class Teclado(DispositivoEntrada):
    cont_tec = 0

    def __init__(self, entrada, marca):
        super().__init__(entrada, marca)
        Teclado.cont_tec += 1
        self.__cont_tec = Teclado.cont_tec

    def __str__(self):
        return f"Teclado= ID: {self.__cont_tec} {super().__str__()}"



