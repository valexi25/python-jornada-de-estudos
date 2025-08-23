print('**** Sistema de Inventarios ***')

inventario = []
numero_productos = int(input('Ingresa a cantidad de proditos a registrar: '))

for indice in range(numero_productos):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Ingresa el precio: '))
    cantidad = int(input('Cantidad: '))
    #Creamos el dicionario con el detalle del producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    #Agregamos el nuevo producto  al inventario
    inventario.append(producto)

#Mostrar el inventario inicial
print(f'\n Inventario inicial: {inventario}')

#Buscar um producto por id
id_buscar = int(input('\nIngrsa el Id del producto a buscar: '))
producto_encontrado = None

for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print('Informacion del producto encontrado: ')
    print(f''' 
    Id: {producto_encontrado.get('id')}
    Nonbre: {producto_encontrado.get('nombre')}
    Precio: R${producto_encontrado.get('precio'):.2f}
    Cantidad: {producto_encontrado.get('cantidad')}\n''')
else:
    print(f'Producto con id {id_buscar} NO encontrado ') 

#mostramos el inventario detallado
print('Inventario em estoque\n')
for producto in inventario:
    print(f''' 
    Id: {producto.get('id')}
    Nombre: {producto.get('nombre')}
    Precio: R${producto.get('precio'):.2f}
    Cantidad: {producto.get('cantidad')}
''')