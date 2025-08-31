print('*** Calculadora de Impuestos ***')

# Funcion qque calcula el total de um pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto,inpuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto *(inpuesto/100)
    return pago_total

#Ejecutar nuestra funcion
pago_sin_inpuesto = float(input('Proporcione el pago sin impuesto: '))
inpuesto = float(input('Proporcione el monto del impuesto: '))
pago_con_impuesto = calcular_total_pago(pago_sin_inpuesto,inpuesto)
print(f'Pago com impuesto: {pago_con_impuesto}')