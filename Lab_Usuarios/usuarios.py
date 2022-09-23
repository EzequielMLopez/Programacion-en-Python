class Usuario():

    def __init__(self, id_usuario=None, username=None, password=None):
        self.__id = id_usuario
        self.__username = username
        self.__password = password

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @id.setter
    def id(self, nuevo):
        self.__id = nuevo

    @username.setter
    def username(self, nuevo):
        self.__username = nuevo

    @password.setter
    def password(self, nuevo):
        self.__password = nuevo

    def __str__(self):
        return(f"""ID: {self.__id}  USERNAME: {self.__username}  PASSWORD: {self.__password}""")

if __name__ == "__main__":
    pass
    #personas = []
    #persona1 = Usuario(15, "Sandro", "Sandrito")

    #for i in range(0,10):
    #    personas.append(Usuario(i, f"a{i}", f"zxc{i}"))

    #for persona in personas:
    #    print(persona)




