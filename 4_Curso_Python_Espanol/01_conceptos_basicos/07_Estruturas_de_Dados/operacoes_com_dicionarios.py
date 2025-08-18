print("*** Dicionario en Python ***")

#creamos un dict de persona con clave y valor
persona = {
    'nombre': 'Sergio',
    'edad':30,
    'ciudad': 'Mexico'
}

print(f'Dicionario de persona:{persona}')

#podemos aceder a los elemento del dicionario
print(f'Nombre: {persona["nombre"]}')
print(f'edad: {persona.get("edad")}')
print(f'Ciudad: {persona.get("ciudad")}')

#modificar un valor del dicionario
persona['edad'] = 35
print(f'edad: {persona.get("edad")}')

print(f'Dicionario de persona: {persona}')

#Agregar un nuevo elemento 
persona['profesion'] = 'Ingeniero'
print(f'Diccionario de perssona: {persona}')

#eliminar um elemento de dicionario
del persona['ciudad']
print(f'Eliminar um elemento {persona}')

persona.pop('profesion')
print(f'Eliminando profesion: {persona}')
#Itera los elemento del un dict (llave,valor)
for llave, valor in persona.items():
    print(f'la llave associada {llave} valor associado {valor}')

#obtener los valores
print(f'\nValor del dicionario') 
for valor in persona.values():
    print(f'Valor - {valor}')

#Obter las llaves 
print(f'Impresión de las llaves de Dicionarios')
for llave in persona.keys():
    print(f'- {llave}')

