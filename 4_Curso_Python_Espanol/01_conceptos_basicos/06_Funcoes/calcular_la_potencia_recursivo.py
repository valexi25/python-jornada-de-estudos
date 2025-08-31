print('**** Calcular la potencia de un número con metodo reclusivo ****')

#Funcion potencia de un numero
def potencia(base,exponente):
    #caso base
    if exponente == 0:
        return 1
    else: #caso recursivo
        return base * potencia(base,exponente - 1)

#Llamada la funcion
print(f'2 elevado a la 3 = {potencia(2,3)}')
print(f'5 elevado a la 1 = {potencia(5,0)}')
print(f'4 elevado a la 5 = {potencia(4,5)}')