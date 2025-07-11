print('*** Valor Dentro de Rango ***')
"""
    Solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionado está dentro de rango 

    se deben definir 2 constantes, valor_minimo = 0 y valor_maximo =

    y debemos comprobar si el valor proporcionado se encuentra en el rango entre 0 y 5

    finalmente se debe imprimir/. 
        valor dentro de rango: true/false
"""
VALOR_MAXIMO = 5
VALOR_MINIMO = 0 

valor_porpocionado = int(input("Ingrese un valor: "))
#rango = ((VALOR_MINIMO >= valor_porpocionado) and (valor_porpocionado <= VALOR_MAXIMO))
rango = VALOR_MINIMO <= valor_porpocionado <= VALOR_MAXIMO
print(f"Valor dentro de rango? {rango}")