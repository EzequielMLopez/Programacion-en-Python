from DispositivoEntrada import *

class Raton(DispositivoEntrada):
    cont_raton = 0

    def __init__(self, entrada, marca):
        super().__init__(entrada, marca)
        Raton.cont_raton += 1
        self.__cont_raton = Raton.cont_raton

    def __str__(self):
        return f"Raton= ID: {self.__cont_raton} {super().__str__()}"

