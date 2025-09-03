print('**** Funcion par ***')

#Funcion para saber si un numero es par o no

def es_par(numeros):
    if numeros % 2 == 0:
        return True
    else:
        return False

#Llamamos a la funcion
if __name__ == '__main__':
    numero = int(input('Proporciona un numéro entero: '))
    print(f'Número par? {es_par(numero)}')