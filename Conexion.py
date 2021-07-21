from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE='test_db'
    _USERNAME='postgres'
    _PASSWORD = 'virus'
    _DB_PORT='5432'
    _HOST='localhost'
    _MIN_CON=1
    _MAX_CON=5
    _pool=None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON, host= cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database=cls._DATABASE
                                                      )
                log.debug(f'conexion establecida con exito {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'ha ocurrido un errror al obtener el poool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion =cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pul con exito {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'se libero la conexion {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

if __name__ == '__main__':
    con1= Conexion.obtenerConexion()
    con2=Conexion.obtenerConexion()
    Conexion.liberarConexion(con1)