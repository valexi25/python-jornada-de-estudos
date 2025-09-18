import psycopg2

conexion = psycopg2.connect(user='postgres',password='sua-senha',host='host',port='port',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan','peres','Jperes.com',1),
                ('Ivonne','gutierrez','iguttieres@gmail.com',2),
                )
            cursor.executemany(sentencia,valores)
            redistro_atualixados = cursor.rowcount
            print(f'Registros atualizados: {redistro_atualixados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()