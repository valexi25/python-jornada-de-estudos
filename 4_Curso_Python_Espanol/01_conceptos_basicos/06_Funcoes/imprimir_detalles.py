print("&&& Imprimir detalles de una persona usando Kwargs")

# Funcion que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalles_persona(**kwargs):
    print('\nVAlores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

#llamamos a la funcion
imprimir_detalles_persona(nombre='Karla',edad=30,ciudad='Mexico' )
imprimir_detalles_persona(nombre='carlos',edad=20,ciudad='Mexico',puesto='gerente')