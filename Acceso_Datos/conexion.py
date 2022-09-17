import sys
import mysql.connector
from logger import log

class Conexion():
    __host = "xxx"
    __user = "xxx"
    __pass = "xxx"
    __db = "xxx"
    __conexion = None
    __cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion == None:
            try:
                cls.__conexion = mysql.connector.connect(
                                                        host=cls.__host,
                                                        user=cls.__user,
                                                        passwd=cls.__pass,
                                                        db=cls.__db)
                
                
                log.debug(f"Conexion exitosa: {cls.__conexion}\n")
                return cls.__conexion
            except Exception as e:
                log.error(f"Ocurrio el siguiente error: {e}")
                sys.exit()
        else:
            return cls.__conexion

    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor == None:
            try:
                cls.__cursor = cls.obtenerConexion().cursor()
                log.debug("El cursor se creo exitosamente\n")
                return cls.__cursor

            except Exception as e:
                log.error(f"Ocurrio el siguiente error: {e}")
                sys.exit()
        else:
            return cls.__cursor

if __name__ == "__main__":
    con = Conexion()
    con.obtenerConexion()
    con.obtenerCursor()