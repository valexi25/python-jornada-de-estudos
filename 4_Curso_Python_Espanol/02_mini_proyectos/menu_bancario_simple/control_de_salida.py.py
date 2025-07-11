print("*** Sistema Bancario***")
"""
Considerando que estamos dentro de un sistema bancario, se solicita perguntar al usuario si desea continuar dentro del sistema.

Utilizando el operador not para aplicar una lógica inversa se debe programar las siguientes condiciones:
    Si no deseamos salir del sistema,imprimir:
        continuamos dentro del sistema
        De lo contrario, imprimimos saliendo del sistema
"""
salir_sistema_txt = input("Deseas salir del sistema (si/no)? ")
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print("Continuamos dentro del sistema")
else:
    print('Salimos del sistema')