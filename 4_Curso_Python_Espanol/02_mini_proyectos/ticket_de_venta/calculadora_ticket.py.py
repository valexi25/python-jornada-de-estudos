print('*** Generación ticket venta ****')
"""
supongamos que compramos varios artículos en el supermercado y queremos obtener el tiket de venda total incluyendo impuestos.

el sistema solicitará el precio de cada producto a comprary el usuario deverá indicar su precio(valor de tipo con punto decimal)

el sistema debe realizar la suma de cada producto, calcular el impuesto y finalmente imprimir el total de la compra
"""
precio_leche = float(input("precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio de lechuga"))
precio_platanos = float(input("Precio plátanos: "))
descuento_porcentaje = int(input("Aplicar algún descuento (%)?"))


#cáculo del sudtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos
# Aplicar el descuento
descuento = subtotal * (descuento_porcentaje/100)

subtotal_con_descuento = subtotal - descuento

# Calculo con impoesto (16%)
impuesto = subtotal_con_descuento * 0.16

# Calculo total de la compra (com impuestos)
costos_total_compra = subtotal_con_descuento + impuesto
print(f"""
Subtotal: ${subtotal:.2f}
Descuento: ${descuento} ({descuento_porcentaje}%)
subtotal con descuento: ${subtotal_con_descuento}
impuesto (16%): ${impuesto:.2f}
costo total de la compra: ${costos_total_compra:.2f}
""")
