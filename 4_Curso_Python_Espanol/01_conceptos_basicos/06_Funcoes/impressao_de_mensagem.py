print("**** Repetición de Mensaje ***")

mensaje = input('Porporciona un mensaje a repetir: ')
numero_de_repeticiones = int(input('Porporciona el nùmenro de repeticiones: '))

for i in range(numero_de_repeticiones):
    print(f'{i+1} - {mensaje}')