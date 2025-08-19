print('*** Agendad de Contatos')
agenda = {
    'carlos':{
        'telefono':'5557667711',
        'email': 'carlos@gamil.com',
        'direcion': 'caller povas 32'
    },
    'maria':{
        'telefono': '324343423',
        'email': 'maria@gamil.com',
        'direcion': 'calle barros'
    },
    'pedro':{
        'telefono': '212334343',
        'email': 'pedro@gmail.com',
        'direcion':'calle pombas'
    }
}

print(agenda)

#acceder a la informacion de un contacto espesifico
print(f'''Información del contacto de Maria:
    Telefono: {agenda["maria"]["telefono"]}
    Email: {agenda.get('maria').get('email')}
    Direccion: {agenda.get("maria").get('direcion')}

''')
#agregar a un nuevo contacto 
agenda['ana'] = {
    'telefono': '5555555555',
    'email': 'ana@mail.com',
    'direcion': 'calle nueva'
}
print(f'agenda: {agenda}')
#Eliminar un contacto exixtente 
agenda.pop('pedro')
print()
#del agenda['pedro']
print(f'agenda: {agenda}')
#Mostramos los contactos de la agenda
print('\nContactos en la agenda')

for nombre, detalles in agenda.items():
    print(f"""Nombre: {nombre}
    Tel0éfono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Direccion:{detalles.get('direcion')}
""")