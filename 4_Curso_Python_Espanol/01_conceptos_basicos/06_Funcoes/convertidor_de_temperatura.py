print('----- Convertidor de temperatura -----')
#Funcion que convierte de celsius a fahreneit
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenhit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Realizamos algunas pruebas de conversion
celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
#Imprimios el resultado 
print(f'{celsius} C a F: {resultado:.2f}')


#Realizamos la pruebe de fahrenheit a celsius
fahrenheit = float(input('Proporciona su valor en farenheit: '))
resultado = fahrenhit_celsius(fahrenheit)
#Imprimimos el resultado
print(f'{fahrenheit} F a C: {resultado:.2f}')