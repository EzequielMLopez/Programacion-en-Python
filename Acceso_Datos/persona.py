from logger import log

class Persona():

    def __init__(self, IDs=None, Nombre=None, Apellido=None, Email=None):
        self.__id = IDs
        self.__nombre = Nombre
        self.__apellido = Apellido
        self.__email = Email

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__nombre

    @property
    def lastname(self):
        return self.__apellido

    @property
    def email(self):
        return self.__email

    @id.setter
    def id(self, newid):
        self.__id = newid

    @name.setter
    def name(self, newname):
        self.__nombre = newname

    @lastname.setter
    def lastname(self, newlastname):
        self.__apellido = newlastname

    @email.setter
    def email(self, newemail):
        self.__email = newemail

    def __str__(self):
        return(f"""
        ID Persona: {self.__id}, Nombre: {self.__nombre}
        Apellido: {self.__apellido}, Email: {self.__email}\n""")

if __name__ == "__main__":
    roberto = Persona(1, "Roberto", "Gutierrez", "ld,asl@dlas,d.com")
    log.debug(roberto)
    # Simular un insert 
    roberto = Persona(Nombre="Roberto", Apellido="Gutierrez", Email="ld,asl@dlas,d.com")
    log.debug(roberto)
    # Simular delete
    roberto = Persona(ID=1)
    log.debug(roberto)
    