class DispositivoEntrada:
    def __init__(self, entrada, marca):
        self._tipoent = entrada
        self._marca = marca 

    @property
    def tipoent(self):
        return self._tipoent

    @property
    def marca(self):
        return self._marca

    @tipoent.setter
    def tipoent(self, nuevo):
        self._tipoent = nuevo

    @marca.setter
    def marca(self, nuevo):
        self._marca = nuevo

    def __str__(self):
        return f"Tipo: {self._tipoent} Marca: {self._marca}"



