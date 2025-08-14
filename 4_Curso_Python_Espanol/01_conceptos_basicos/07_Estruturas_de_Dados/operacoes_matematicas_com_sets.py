print("*** Operaciones con tipo sets")
a = {1,2,3,4}
b = {3,4,6,7}

union = a | b

print(f'Union de a y b: {union}')

#Intercecion

intercescion = a & b
print(f'Interceccion de a com b {intercescion}')

#Diferencia 
diferencia = a - b
print(f'Diferencia de a com b {diferencia}')