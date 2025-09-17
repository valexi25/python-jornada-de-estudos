from numeros_identicosException import NumerosIdenticosException

resultado = None

try: 
    a = int(input('Primer número: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('número identicos')
    resultado = a/b
except Exception as e:
    print(f'Ocurrio un erros: {e}')
except TypeError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e}, {type(e)}')
else:
    print('No se arrojo ninguna excepción')
finally:
    print('Ejecución de bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos.....')