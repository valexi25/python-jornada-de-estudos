print('*** Regresar una tupla de valores desde una funcion *****')

#Definir de la funcion
def persona_mayusculas(nombre,apellido,edad):
    print(f'Esta función regresa varios valores (tuplas)')
    return nombre.upper(),apellido.upper(),edad

# Programa principal     
nombre,apellido,edad = persona_mayusculas('Sandra','Jimenez',42)
print(f'\nResultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {42}')