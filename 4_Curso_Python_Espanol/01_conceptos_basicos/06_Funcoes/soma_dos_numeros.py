print('*** Suma iterativa ***')

# Sumar los primeiro 5 numeros

MAXIMO = 5
numero = 1
acumulador_soma = 0
#Empezamos a iterar
while numero <= MAXIMO:
    acumulador_soma += numero
    numero += 1
    print(f"{acumulador_soma}",end=',')

print(f'\n Resultado de las sumas acumuladas {acumulador_soma}')