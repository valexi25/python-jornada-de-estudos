print('*** Ejemplo dentro de rango ***')
#revisar si una variable se encuentra dentro de ramgo 1 y 10 
dato = int(input('Proporciona un dato enteito: '))

#revisar si está dentro de rango
esta_dentro_rango = 1 <= dato <= 10
#print(f'Variabel está dentro de rango (entre 1 y 10)?: {esta_dentro_rango}')

#revisamos la lógiva inversa, si el dato esta fuera de rango 
esta_dentro_rango = not(1 <= dato <= 10)
print(f"variable esta fuera de rango (ente 1 y 10)? {esta_dentro_rango}")
