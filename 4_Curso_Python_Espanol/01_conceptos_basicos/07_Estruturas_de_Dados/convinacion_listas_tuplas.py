print('*** convinacion de listas e tuplas ***')

#definir una lista que almacena tuplas de productos
productos = [
    ('P001','Camiseta', 20.00),
    ('P002','jeans',30.00),
    ('P003','Sudadera',40.00)
]

# Imprimir la informacion de cada producto
# y ademas calculamos el precio total

precio_total = 0

print('Informacion de los productos: ')
for producto in productos:
    #print(producto)
    id,descricion,precio = producto
    print(f'Productos: id = {id}, descripcion = {descricion}, precio = R${precio:.2f}')
    precio_total += precio 
print(f'Precio Total de los productos: R${precio_total:.2f}')