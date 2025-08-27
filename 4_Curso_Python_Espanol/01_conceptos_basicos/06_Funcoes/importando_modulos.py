print("*** Función sumar ****")

# Definimos la funcion
def sumar(a,b):
    resultado_suma = a + b
    return resultado_suma


# Prueva a la funcion sumar
if __name__ == '__main__':
    print(f"Prueba función sumar desde el módulo: {sumar(15,30)}")