print('*** Calculadora con Funciones ****')

def mostar_menu():
    print(f'''\nOperaciones que puedes realizar:
    1. Suma.
    2. Resta.
    3. Multiplicación.
    4. Divición.
    5. Salir''')
    opcion = int(input('Escoge una opción: '))
    return opcion

def sumar(oprerando1,operqndo2):
    resultado = oprerando1 + operqndo2
    print(f'El resultado de la suma de {oprerando1} + {operqndo2} = {resultado}')

def restar(operando1,operando2):
    resultado = operando1 - operando2
    print(f'El resultado de la resta de {operando1} - {operando2} = {resultado}')

def multiplicar(operando1,operando2):
    resultado = operando1 * operando2
    print(f'El resultado de multiplicacion de {operando1} * {operando2} = {resultado}')

def dividir(operando1,operando2):
    resultado = operando1 / operando2
    print(f'El resultado de la divicion de {operando1} / {operando2} = {resultado}')

def pedir_valores():
    operando1 = float(input('Ingrese el operando numero 1: '))
    operando2 = float(input('Ingrese el operando numero 2: '))
    return operando1,operando2

def ejecutar_operacion(opcion,salir):
    #Solicitar los valores de los operandos
    if 1 <= opcion <= 4:
        operando1,operando2 = pedir_valores()
    resultado = 0
    if opcion == 1:
        sumar(operando1,operando2)
    elif opcion == 2:
        restar(operando1,operando2)
    elif opcion == 3:
        multiplicar(operando1,operando2)
    elif opcion == 4:
        dividir(operando1,operando2)
    elif opcion == 5:
        print("Saliendo hasta luego!!!")
        salir = True 
    else: 
        print('Opcion nao encontrada')
    return salir


if __name__ == "__main__":
    salir = False
    while not salir:
        opcion = mostar_menu()
        salir = ejecutar_operacion(opcion,salir)
      