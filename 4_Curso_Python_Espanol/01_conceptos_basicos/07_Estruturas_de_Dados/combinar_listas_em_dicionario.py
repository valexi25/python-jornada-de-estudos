print('**** Lista y Dicionarios ***')

personas= [
    {
        'nombre':'Regina',
        'apellido': 'Flores',
        'edad':21
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad':32
    }
]


print(personas)
#Aceder a un diccionario desde una lista
print(f'''
    Nombre: {personas[0].get('nombre')}
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}
''')

print(f'''
    Nombre: {personas[1].get('nombre')}
    Apellido: {personas[1].get('apellido')}
    Edad: {personas[1].get('edad')}
''')
#Recorer los elemntos de la lista
print()
for contador, persona in enumerate(personas):
    print(f'{contador} - Persona: {persona}')
    print(f'Detalle: Nombre: {persona.get("nombre")}, Apellido: {persona.get("apellido")}')