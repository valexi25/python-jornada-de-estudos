import psycopg2

conexion = psycopg2.connect(user='postgres',password='sua_senha',host='host',port='PORT',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona in %s'
            entrada = input('Proporciona los ID\'s a eliminar(separados por ,): ')
            valores = (tuple((entrada.split(',')),),)
            cursor.execute(sentencia,valores)
            redistro_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {redistro_eliminados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
    