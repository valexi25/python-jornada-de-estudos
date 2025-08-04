"""
Cear un programa para indicar cual es el mayor de dos números.
el mayor de dos números.
El programe debe pedir al usuario dos números enteros.
Posteriormente se deben comparar y mandar a imprimir el número mayor.
"""
print("*** El mayor de dos números****")
numero1 = int(input("Proporciona el número 1: "))
numero2 = int(input("Proporciona el segundo Número"))
#El mayor de dos números
if numero1 > numero2:
    print(f"El numero 1 es mayor: {numero1}")
else:
    print(f'El numero 2 es mayor: {numero2}')