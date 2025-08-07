from random import randint
    
print('*** Juego de Adivinanzas ****')

nuemero_secreto = randint(1,50)
intentos = 0
adivinanza = None
INTENTOS_MAXIMO = 5
while adivinanza != nuemero_secreto and intentos < INTENTOS_MAXIMO:
    adivinanza = int(input('Adivina el numero secreto (1 - 50):  '))
    if adivinanza < nuemero_secreto:
        print('El número secreto es mayor')
    elif adivinanza > nuemero_secreto:
        print('El número Secreto es menor')
    intentos += 1
if adivinanza == nuemero_secreto:
    print(f'Felicidades adicvinaste el numero secreto {nuemero_secreto} em {intentos} intentos')
else:
    print(f'Lo siento, has agotado el número de intentos màximos: {INTENTOS_MAXIMO}')
    print(f'El nùmero secreto era: {nuemero_secreto}')