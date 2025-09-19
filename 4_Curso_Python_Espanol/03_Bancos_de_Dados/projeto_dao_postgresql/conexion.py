from logger_base import log
from psycopg2 import pool
import sys 
class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'senha'
    _DB_PORT = '3636'
    _HOST = '198.162.0.32'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
   
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
          try:
            cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,host = cls._HOST,user = cls._USERNAME,password = cls._PASSWORD,port = cls._DB_PORT,database=cls._DATABASE)
            log.debug(f'Creación del poll exitosa: {cls._pool}')
            return cls._pool
          except Exception as e:
            log.error(f'Ocurrio un errore al obtener el pool {e}')
            sys.exit()
        else:
          return cls._pool

    @classmethod
    def obtenerConexion(cls):
      conexion = cls.obtenerPool().getconn()
      log.debug(f'Conexión obtenida del pool: {conexion}')
      return conexion
    
    @classmethod
    def liberarConexion(cls,conexion):
       cls.obtenerPool().putconn(conexion)
       log.debug(f'Regresamos la conexión al pool de conexion')

    @classmethod
    def cerrarConexiones(cls):
       cls.obtenerPool().closeall()

if __name__ == '__main__':
    conecion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conecion1)
    cpnecion2 = Conexion.obtenerConexion()
    cpnecion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(cpnecion3)
    cpnecion4 = Conexion.obtenerConexion()
    cpnecion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(cpnecion5)
    cpnecion6 = Conexion.obtenerConexion()


   