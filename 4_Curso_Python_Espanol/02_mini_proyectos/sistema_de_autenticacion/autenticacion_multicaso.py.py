"""
    Sistema de autenticación 
    Crear un sistema para validar los valores de usuario y password proporcionados.

    Se deben definir dos constantes con valores Válidos de usuarios y password

    y el sistema debe comparar los valores validos contra los valores proporcionados
    se deben considerar 4 casos
        Usuario y password válidos. debe imprimir bienvenido al sistema

        usuario invalido 

        password invalido 

        usuario y password invalidos
"""

USUSARIO_VALIDO = "alex"
PASSWORD_VALIDO= "1234"

usuario = input('Ingrese el usuario: ')
password = input('Ingrese la contraseña')
usuario.strip().lower()
password.strip().lower()

if usuario == USUSARIO_VALIDO and password == PASSWORD_VALIDO:
    print("Bienvenido al sistema")
elif usuario != USUSARIO_VALIDO:
    print("Ususario invalidos")
elif password != PASSWORD_VALIDO:
    print("Contraseña invalida")
else:
    print("Contraseña y usuarios invalidos")

