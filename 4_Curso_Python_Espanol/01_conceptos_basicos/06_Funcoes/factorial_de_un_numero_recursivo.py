print('*** Factorial de un número con recursividad ***')
# Definimos la funcion fatorial recurciva
def factorial_recurciva(numero):
    # Caso base, factorial 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f'Resultadp factorial parcial {numero} es : 1')
        return 1
    else: #caso recursivo
        factorial_parcial = numero * factorial_recurciva(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

resultado = factorial_recurciva(5)