print('*** Obtener Coordenasdas x,y,z *****')

def obtener_coodenadas():
    x,y,z = 10,20,30
    return (x,y,z)

#Llamar la funcion
resultado = obtener_coodenadas()
print(resultado)

# Unpacking de la tupla
x1,y1,z1 = resultado

print(f'las coodenadas x = {x1}, y = {y1}, z = {z1}')