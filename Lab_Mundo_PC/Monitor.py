class Monitor():
    cont_mon = 0

    def __init__(self, marca, tamaño):
        Monitor.cont_mon += 1
        self.__cont_mon = Monitor.cont_mon
        self.__marca = marca
        self.__tamaño = tamaño

    @property
    def marca(self):
        return self.__marca

    @property
    def tamaño(self):
        return self.__tamaño

    @marca.setter
    def marca(self, nuevo):
        self.__marca = nuevo

    @tamaño.setter
    def tamaño(self, nuevo):
        self.__tamaño = nuevo

    def __str__(self):
        return f"Monitor= ID: {self.__cont_mon} Marca: {self.__marca} Tamaño: {self.__tamaño}"


