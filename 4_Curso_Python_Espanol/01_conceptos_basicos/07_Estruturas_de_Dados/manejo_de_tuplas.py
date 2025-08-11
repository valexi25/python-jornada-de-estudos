print('*** Manajo de Tuplas ****')

mi_tupla = (1,2,3,4,5)
print(mi_tupla)
#No podemos modificar
#mi_tupla[0] = 10
#Iterar los elementos de una tupla
for elemento in mi_tupla:
    print(elemento, end=' ')   
    
#Crear una tupla para una coordenada x,y
coordenada = (3,5)
print(f'\nCoordenada en el eje x: {coordenada[0]} ')
print(f'Coodenada en el eje y: {coordenada[1]}')

tupla_unitaria = 10,
print(f'Tupla de un elemento {tupla_unitaria}')

#tupla anidada
tuplas_anidada = (1, (2,3),(4,5))
print(f'Segundo elemento de la tupla anidada {tuplas_anidada[1]}')