print('**** Calculadora ****')

salir = False
operando1 = operando2 = resultado = 0
while not salir:
    print('''Operaciónes que puedes hacer
          1. Sumar
          2. restar
          3. multiplicar
          4. divicion
          5. salir''')
    opcion = int(input("Escoje una opción: "))
    # pedir operadores
    if 1 <= opcion <= 4:
        operando1 = float(input('Numero 1:'))
        operando2 = floar( input('Numero 2:'))
    if opcion == 1:
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado:.2f}\n')
    elif opcion == 2:
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado:.2f}\n')
    elif opcion == 3:
        resultado = operando1 * operando2
        print(f'El resultado de la Multiplicación es: {resultado:.2f}\n')
    elif opcion == 4:
        resultado =  operando1 / operando2
        print(f'El resultado de la divicion es: {resultado:.2f}\n')
    elif opcion == 5:
        print('Saliendo de la carculadora')
        salir = True
    else:
        print('Operacion invalida')
else:
    pass