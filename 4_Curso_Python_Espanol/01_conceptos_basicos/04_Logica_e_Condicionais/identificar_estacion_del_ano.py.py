"""
Se solicita proporcionar el valor de un me (valor numérico entre 1 y 12)
e indicar la estación del año segun lo siguiente:
    meses 1,2 o 12 -> invierno
    meses 3,4 o 5 -> primavera
    meses 6,7 u 8 -> verano
    meses 9,10 u 11 -> otono
Cualquer otro valor -> Estación Desconecida
"""
print("**** Estacion del año ****")
mes = int(input('Porporciona el valor del mes (1-12)'))
estacion = None

# Revisión del mes proporcionado

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes ==5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes ==8: 
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Estacion desconocido'

#Imprimir el resultado
print(f"La estación para el mes {mes} es {estacion}")