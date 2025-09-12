print('**** Maquina de Snacks ***')
#definimos la lista de snacks inicial
snacks = [
    {'id': 1 ,'nombre':'Papas','precio':30},
    {'id':2,'nombre':'Refresco','precio':50},
    {'id':3,'nombre':'Sandwich','precio':120}
]
# Lista de productos (vacia). Son los ya comprados
productos = []

def mostrar_snacks():
    print('--- Snachs Disponibles ---')
    for snak in snacks:
        print(f'\t Id: {snak.get("id")} -> {snak.get("nombre")}'
            f' - ${snak.get("precio")}')
        
def buscar_snack_por_id(id_buscar):
    for snack in snacks:
        if snack.get('id') == id_buscar:
            return snack
    #si llegamos al final y no se encontro el snack regresa None
    return None
    
def comprar_snacks():
    id_snack = int(input('Qué snack quieres comprer (id): '))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack No encontrado con el id: {id_snack}')
    
def mostrar_ticket():
    tiket = f'\t--- Ticket de Venda ----'
    total = 0
    for producto in productos:
        tiket += f"\n\t- {producto.get('nombre')} - ${producto.get('precio')}"
        total += producto.get('precio')
    tiket += f'\n\tTotal -> ${total}'
    print(tiket)

if __name__ == '__main__':
    #Creamos el menu
    while True:
        print('''Menú:
        1. Mostrar Snacks.
        2. Comprar Snack.
        3. Mostrar ticket.
        4. Salir.''')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snacks()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Saliendo del sistema hasta luego !!!!')
            break
        else:
            print('Opción inválidad proporciona otra opción!!')
        