import mysql.connector
personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password = 'admin',
    database='perosonas_db'
)

mi_cursor = personas_db.cursor()
mi_cursor.execute('SELECT nombre,apellido,edad FROM personas')
resultado = mi_cursor.fetchall()
for persona in resultado:
    print(persona)

personas_db.close()