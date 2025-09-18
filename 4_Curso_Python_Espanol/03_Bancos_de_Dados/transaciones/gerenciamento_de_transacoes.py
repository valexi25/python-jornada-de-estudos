import psycopg2 as bd

conexion = bd.connect(user='postgres',password='senha',host='host',port='port',database='test_db')
try:
    with conexion:
    #conexion.autocommit = False
        with conexion.cursor() as cursor:   
            sentencia = 'Insert into persona (nombre,apellido,email) VALUES(%s,%s,%s)'
            valores = ('marcos','almada','mesparza@gmail.com')
            cursor.execute(sentencia,valores)
            sentencia ='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
            valores = ('Juan','peres','jcjuarez@gmail.com',1)
            cursor.execute(sentencia,valores)
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se iso rollbal de la transacion: {e}')
finally:
    conexion.close()
    


print('Termina la transancion se hico comit')
