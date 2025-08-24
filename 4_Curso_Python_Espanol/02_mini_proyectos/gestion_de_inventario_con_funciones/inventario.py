print('*** Sistema de inventario con funciones ****')
# Inventario del almacen
inventario = [
    {'id':1, 'nombre': 'Camisa','precio': 25.99,'cantidad': 50},
    {'id':2, 'nombre': 'Pantalon','precio': 50.99,'cantidad': 150},
    {'id':3, 'nombre': 'Cama','precio': 225.99,'cantidad': 250}
]

# Funcion para mostrar el inventario
def mostrar_inventario():
    print('--- Inventario del Almacém ----')
    for producto in inventario:
        print(f'Id: {producto.get("id")}, Nombre: {producto.get("nombre")},'
              f'Precio: ${producto.get("precio")},Cantidad: {producto.get("cantidad")}')

def agregar_producto():
    print('-- Agregar Nuevo Producto ---')
    id = int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id':id,'nombre':nombre,'precio':precio,'cantidad':cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')


def buscar_producto_por_id():
    print('--- Buscar Producto po Id ---')
    id_buscar = int(input('Ingresa el id a buscar: '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print('\nInformación del producto encontrado: ')
            print(f"ID: {producto.get('id')}, Nombre: {producto.get('nombre')},"
                f" Precio: ${producto.get('precio')},"
                f" Cantidad: {producto.get('cantidad')}")
            return
    print('Producto no encontrado')

# Programa Pricipal
if __name__ == '__main__':
    while True:
        print(f'''
        1. Mostrar inventario.
        2. Agregar nuevo producto.
        3. Buscar producto por id.
        4. Salir''')
        opcion = int(input('Proporciona una opción (1-4):'))
        # Revisamos las opciones del menu
        if opcion == 1: # Mostrar el inventario
            mostrar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_producto_por_id()
        elif opcion == 4:
            print('Hata luego!')
            break
        else:
            print('Opción invalida proporciona una opción validad')