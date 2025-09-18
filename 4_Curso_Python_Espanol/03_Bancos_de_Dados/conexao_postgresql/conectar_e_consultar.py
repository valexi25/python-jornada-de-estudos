import psycopg2

conexion = psycopg2.connect(user='postgres',password='sua-senha',host='seu-host',port='porta-escolhida',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona in %s'
            #llaves_primarias = ((1,2,3,4),)
            entrada = input('Proporciona los id\'s a buscar: (separados por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia,llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()