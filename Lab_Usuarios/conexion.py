from mysql.connector import pooling
from logger import *

class PoolConexiones():

    __host = "xxx"
    __user = "xxx"
    __pass = "xxx"
    __db = "xxx"
    __pool_name = "xxx"
    __reset_pool = False
    __max_cont = 2
    __connection_pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.__connection_pool == None:
            try:
                cls.__connection_pool = pooling.MySQLConnectionPool(pool_size=cls.__max_cont,
                                                                    pool_name=cls.__pool_name,
                                                                    pool_reset_session=cls.__reset_pool,
                                                                    host=cls.__host,
                                                                    user=cls.__user,
                                                                    password=cls.__pass,
                                                                    database=cls.__db)
                return cls.__connection_pool

            except Exception as e:
                log.error(f"Ocurrio un error: {e}")

        else:
            return cls.__connection_pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().get_connection()._cnx
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool()._queue_connection(cnx=conexion)

    @classmethod
    def eliminarConexiones(cls):
        canti_elimi = cls.obtenerPool()._remove_connections()
        cls.__connection_pool = None
        log.info(f"Conexiones eliminadas: {canti_elimi}".center(50,"-"))


if __name__ == "__main__":
    pass
    #pool = PoolConexiones().obtenerConexion()
    #PoolConexiones().liberarConexion(pool)
    #pool2 = PoolConexiones().obtenerConexion()
    #PoolConexiones().liberarConexion(pool2)
    #pool3 = PoolConexiones().obtenerConexion()

    #PoolConexiones().eliminarConexiones()
