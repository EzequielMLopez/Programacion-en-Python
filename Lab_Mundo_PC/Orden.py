from Computadora import *
from Monitor import *
from Teclado import *
from Ratón import *

class Orden:
    cont_ord = 0

    def __init__(self, *compus):
        Orden.cont_ord += 1
        self.__cont_ord = Orden.cont_ord
        self.__compus = list(compus)

    @property
    def contord(self):
        return self.__cont_ord

    def agregarComputadora(self, compu):
        self.__compus.append(compu)
        
    '''def __str__(self):
        print(f"Orden:{self.__cont_ord}, Computadoras:")
        for com in self.__compus:
            print(f"""\t{com.nombre}:{com.contpc}
                    {com.monitor}
                    {com.teclado}
                    {com.raton}""")'''

    def __str__(self):
        computadoras_str = ""
        for computadora in self.__compus:
            computadoras_str += computadora.__str__()

        return f"""
        Orden: {self.__cont_ord}
        Computadoras: {computadoras_str}"""
