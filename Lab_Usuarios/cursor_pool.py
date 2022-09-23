from conexion import *

class CursorPool():

    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def __enter__(self):
        self.__conexion = PoolConexiones().obtenerConexion()
        self.__cursor = self.__conexion.cursor()
        return self.__cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, traceback):
        if valor_excepcion:
            self.__conexion.rollback()
            log.error(f"{valor_excepcion} {tipo_excepcion} {traceback}")
        else:
            self.__conexion.commit()
        
        self.__cursor.close()
        PoolConexiones().liberarConexion(self.__conexion)
    
if __name__ == "__main__":
    pass
    #with CursorPool() as cursor:
    #    print("Dentro del bloque with".center(50,"#"))
    #    cursor.execute("SELECT * FROM persona")
    #    print(cursor.fetchall())
        