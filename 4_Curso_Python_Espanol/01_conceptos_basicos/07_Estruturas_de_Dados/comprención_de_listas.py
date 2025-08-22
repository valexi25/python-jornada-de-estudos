print('**** Comprensíon de listas ****')

# Una lista con el cuadreado de cada numero
numeros = [1,2,3,4,5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)

# Lista de numeros pares
numeros = range(10+1)
pares = [x for x in numeros if x % 2 == 0]
print(pares)

#Lista saludo a cada nombre
nombres = ['Ana','Jeromimo','carlos']
saludando = [f'hola {nombre}' for nombre in nombres]
print(saludando)