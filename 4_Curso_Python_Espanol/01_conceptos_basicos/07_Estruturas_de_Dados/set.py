print("** manejo de Sets ***")

#Crear un conjunto 
mi_set = {1,2,3,4,5,4}
print(f'Mi sets: {mi_set}')

#Agregar elementos al set
mi_set.add(6)
mi_set.add(7)
print(f'\n Mi sets: {mi_set}')

#Agregar un elemento duplicado
mi_set.add(3)
print(f"\nMi sets: {mi_set}")

#Eliminar um elemento del conjunto
mi_set.remove(4)
print(f'\nset modificado{mi_set}')

#Iterar elementos de set
for elemento in mi_set:
    print(elemento,end=" ")

#Comprovar si tiene elemento en el set
print(f'\n existe el valor {1 in mi_set}')

# Obtener la longitud del set
print(f"El largo del conjunto es: {len(mi_set)}")