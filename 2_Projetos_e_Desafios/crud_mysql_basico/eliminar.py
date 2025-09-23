import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'perosonas_db'
)
cursor = personas_db.cursor()
sentencia_sql = ('DELETE FROM personas WHERE id=%s')
valores =(6,)
cursor.execute(sentencia_sql,valores)
personas_db.commit()
print('Se a eliminado el registro de la base de datos')
personas_db.close()