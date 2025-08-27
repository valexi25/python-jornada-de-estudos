print('*** Alcanse de variables ***')
contador_global = 0

def incrementar_contador():
    #Declaramos una variable local
    contador_local = 0

    # usar a variable global
    global contador_global
    contador_global += 1

    #incrementrar a variable local
    contador_local += 1

    #Imprimimos ambos contadores
    print(f'Contador local: {contador_local}')
    print(f'Concador global: {contador_global}')


# Llamamos variaveces la funcion    
incrementar_contador()
incrementar_contador()


# terminando el programa
print(f'Imprimir el valor final de globla {contador_global}')