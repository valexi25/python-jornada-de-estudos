"""
        Systema  de calificaciones 
cear un programa para convertir una calificación númerica (entre 0 y 10) a una letra (de la F a la A)
        Orientaciones 
si es mayor o igual a 9 y menor o igual a 10 e una A
si es mayor o igual a 8 y menor a 9 es una B
si es mayor o igual a 7 y menor a 8 es una C
si es mayor o igual a 6 y menor a 7 es una D
si es mayor o igual a 0 y menor a 6 es una F
En otro caso, Valor Desconocido
"""
print("*** Sistemas de calificaciones ***")
nota = float(input("Qual es la nota del alumon"))
calificacion_letra = None
if 9 <= nota <= 10:
    calificacion_letra = "A"
elif 8 <= nota <  9:
    calificacion_letra = "B"
elif 7 <= nota < 8:
    calificacion_letra = "C"
elif 6 <= nota < 7:
    calificacion_letra = "D"
elif 0 <= nota < 6:
    calificacion_letra = "F"
else:
    calificacion_letra = "valor desconecido..."

#Imprimir resultado
print(f"Calificacion {nota} es equivalente a {calificacion_letra}")