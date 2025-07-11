print("*** Sistema de Autenticación ***")
"""
crear un programa para validar el usuario y password proporcionados po el usuario
 
crea 2 constantes con los valores correctos y posteriormente con los valores correctos y posteriormente comparar que el usuario sean
válidos.

Debe solicitar el usuario y el password al usuario y si son iguales que los valores correctos almacenados en las constantes debe imprimir FALSE
"""
USUARIO = "admin"
PASSWORD = "123"
usuario_name = input("Ingrese o usuario: ")
passoword_ingresado = input("Ingrese seu passeword: ")
login = (usuario_name.strip() == USUARIO)and(passoword_ingresado.strip() == PASSWORD)
print(f"Dados correctos? {login}")