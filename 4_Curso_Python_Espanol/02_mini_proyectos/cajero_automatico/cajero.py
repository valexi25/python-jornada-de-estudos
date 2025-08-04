print('*** Cajero Automatico ***')

saldo = 1000
salir = False

while not salir:
    print(f'''Operaciones que puedes realizar:
          1. Consultar Saldo
          2. Retirar 
          3. Depositar
          4. Salir''')
    opcion = int(input('Escoje una opión: '))
    if opcion == 1:
        print(f'Tu saldo actual es: ${saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('Ingresa el monto a retirar: '))

        if retiro <= saldo:
            saldo -= retiro
        else:
            print(f'Nocuentas con el saldo suficiente. Saldo actual es: ${saldo:.2f}\n')
    elif opcion == 3:
        deposito =  float(input("Ingresa el monto a depositar: "))
        saldo += deposito
    elif opcion == 4:
        print(f'Saliendo del cajero autommático. Hasta pronto!')
        salir = True
    else:
        print('Opción inválida, Selecciona otra opción\n')
else:
    print('Saliendo del cajero automatico')