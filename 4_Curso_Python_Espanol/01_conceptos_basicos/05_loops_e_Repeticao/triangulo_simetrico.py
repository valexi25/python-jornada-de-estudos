print('Triangulo simetrico ***')

numero_filas = int(input('Porpociona el numero de filhas: '))

# Iterar sobre cada fila del triángulo
for fila in range(1, numero_filas + 1 ):
    espacios_blanco = ' ' * (numero_filas - fila)
    astericos = "*" * (2 * fila - 1)
    print(f'{espacios_blanco}{astericos}')