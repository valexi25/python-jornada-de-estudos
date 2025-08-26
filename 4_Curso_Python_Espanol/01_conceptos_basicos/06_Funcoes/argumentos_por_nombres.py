print('**** Funcion con argumentos por nombre ****')
def imprimir_persona(nombre,apellido = " ", edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad} ')

#Primeiro llamamos la funcion pasando los argumentos de manera posicional

imprimir_persona('Ricardo','Quintana',32 ) 
#Llamar la funcion usando argumentos por nombre
imprimir_persona(nombre='Carlos', apellido='Rojas',edad=28)
#llamar la funcion usando argumentos por nombres. pero intercambiando el orden
imprimir_persona(edad=48,apellido='Manuel',nombre='jose')
#Argumentos con valor por defaul
imprimir_persona(nombre='Carlos')
imprimir_persona(nombre='Carlos',apellido='rojas')
