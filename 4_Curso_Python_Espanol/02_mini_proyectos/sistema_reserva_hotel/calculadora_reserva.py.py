"""
Se solicita crear un sistema de reservación de un hotel se debe pedir lo siguiente información al usuario.
    Nombre de cliente
    Dias de estadia en el hotel 
    cuarto con vista al mar?
El hotel tiene las siguientes tarifas 
    cuarto sin vista al mar $150,50 por dia 
    cuarto con vista al mar 190,50 por dia
El sistema debe calcular el costo total de la estadia dependiendo si escogio el costo un cuarto con vista al mar o no.
"""
print("**** Reserva de Hotel *****")
#VAriavles del hotel
tarifa_diaria_sin_vista_al_mar = 150.50
tarifa_diaria_con_vista_al_mar = 190.50
# Pedimos la informacion al usuario
nombre_cliente = input("Cual es tu nombre: ")
dias_estadia = int(input("Quantos dias de estadias: "))
vista_mar_txt = input('Con vista al mar (si/no)? ')
vista_mar = vista_mar_txt.strip().lower() == 'si'

#calculamos costo total de la estancia
if vista_mar:
    costo_total = dias_estadia * tarifa_diaria_con_vista_al_mar
else:
    costo_total = dias_estadia * tarifa_diaria_sin_vista_al_mar
#Mostramos los detalles de la reserva
print('\n----------Detalles de la Reservación -----')
print(f'\nClientes: {nombre_cliente}')
print(f'Días de estadia: {dias_estadia}')
print(f'Costo total de la reservación: ${costo_total:.2f}')
print(f'Habitación con vista al mar: {"Si"if vista_mar else "No"}')