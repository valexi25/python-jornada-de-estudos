print("*** Lista de suscritores ***")
#definimos set inicial
suscriptores = {}

suscriptores = set()

numero_suscriptores = int(input('Quantos suscriptores vao ser adicionados: '))

for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

print(f'Lista de suscriptores inicial: {suscriptores}')


#veriricaar se um nuevo suscritor esta nalista 
nuevo_suscriptor =  input('Ingrese el nuevo suscrittor (email): ')

if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista: {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo sscritor se a agregado na lista: {nuevo_suscriptor}')
print(f'\nLista de suscriptores {suscriptores}')

#eliminamos un suscritor 
suscritor_eliminar = input('Porporciona el suscriptor a eliminar ')
suscriptores.remove(suscritor_eliminar)
print(f'El suscriptor {suscritor_eliminar} se a eliminado ')
print(f'\nAtualizacion de la lista {suscriptores}')

#verificar la cantidad total de suscriptores
print(f'\nCantidad total de suscriptores: {len(suscriptores)}')

#iterar
for suscriptor in suscriptores:
    print(suscriptor)