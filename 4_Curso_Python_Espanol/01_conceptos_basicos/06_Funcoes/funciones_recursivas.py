print('**** Funciones recurcivas ****')

# DEfinir la funcion recursiva
def funcion_recursiva(numero):
    # Caso Base
    if numero ==1:
        print(numero,end=' ')
    else: #caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=" ")
#programa principal
funcion_recursiva(5)