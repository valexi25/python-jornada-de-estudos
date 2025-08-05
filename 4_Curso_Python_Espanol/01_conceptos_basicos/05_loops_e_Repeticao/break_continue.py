print('**** Break y Continue ****')

#Ejemplo con break
print('Palabra Break')

for numero in range(1,10):
    if numero % 2 == 0:
        print(numero,)
        break


#Ejemlo com continue
print('Palabra Continue')
for numero in range(1,10):
    if numero % 2 == 1 :
        continue

    print(numero)
