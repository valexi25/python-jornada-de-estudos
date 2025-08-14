print('**** Promedio de Calificaciones ****')
total_de_calificaciones = int(input('Porporciona el numero de calificaciones a evaluar: '))
calificaciones =[]

# Iterar las calificaciones 
for indice in range(total_de_calificaciones):
    calificacion = float(input(f'Calificacion[{indice + 1}] = '))
    calificaciones.append(calificacion)

# Imprimimos las calificacione proporcionadas
print(f'\nLas clasificacione proporcionadas son: {calificaciones}')

#calculamos el promedio de las clasificaciones
suma_calificaciones =sum(calificaciones)
promedio = suma_calificaciones / total_de_calificaciones
print(f'\nPromedio de las calificaciones: {promedio:.1f}')