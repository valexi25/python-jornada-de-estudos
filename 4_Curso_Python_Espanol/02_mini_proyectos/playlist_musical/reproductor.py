print('*** Playlist de Canciones ***')

# Creamos la lista vacia
lista_reproduccion = []

nuero_canciones = int(input('Cuantas canciones deseas agragar '))
# iteramos 
for indice in range(nuero_canciones):
    cancion = input(f'Porpociona la cansion {indice + 1}: ')
    lista_reproduccion.append(cancion)

#empezamos a agregar canciones
lista_reproduccion.append('hotel California - eagles')
lista_reproduccion.append('Staying Alive - Bee Gess')
lista_reproduccion.append('Dram on - Aerosmith')
print()
#Ordenar a lisra em ordem alfabetico. sort
#lista_reproduccion.sort(reverse=True)
lista_reproduccion.sort()
print()
#mostra lista de canciones 
print(f'Lista de de reproducion\n {lista_reproduccion}')
print()
for cancion in lista_reproduccion:
    print(f' - {cancion}')

