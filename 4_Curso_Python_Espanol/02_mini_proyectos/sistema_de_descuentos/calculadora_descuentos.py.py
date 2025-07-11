print("*** Tienda en Linea ***")
"""
Crear un Sistema que ofrezca descuentos dependienfo del monto de la compra,
o si es miembro de la tienda.
    Se deben revisar las seguintes condiciones
    º 1 Se ha comprado más de $1000 y es miembro -> Descuento de 10%
    º 2 Se sólo es miembro de la tienda  -> Descuento del 5%
    º 3 Se no es miembro ni compro más de $1000 -> Descuento del 0%
"""
eres_mienbro = input("O comprador es miembro de la tienda: ")
valor_compras = float(input("De cuanto fue la compra: "))


if ((valor_compras >=1000) and (eres_mienbro.strip() == 'si')) :
    print(f"Descuento liberado de 10%")
    desconto = valor_compras*(10/100)
    print(f"\nMonto de la compra: ${valor_compras}")
    print(f"Monto del Descuento: ${desconto} ")
    print(f"Monto final: ${valor_compras-desconto}")
elif((valor_compras >= 1000)or (eres_mienbro.strip() =='si')):
    print(f'Descuento Liberado de 5%')
    desconto = valor_compras*(5/100)
    print(f'\nMonto de la compra: ${valor_compras}')
    print(f"Monto del descuento: ${desconto}")
    print(f"Monto final: ${valor_compras-desconto}")
else:
    print('No fue de esta vez!!!')