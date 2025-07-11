print("*** SISTEMAS DE DESCONTSO VIP ***")

NO_PRODUCTOS_DESCUENTO = 30

cantidad_poductos = int(input("Cuantos productos comprestes hoy?: "))
tienes_membresia = input('Tienes la membresia de la tineda (sim/nao): ')

es_elefible_para_el_desconto = (cantidad_poductos >= NO_PRODUCTOS_DESCUENTO and tienes_membresia.strip().lower() == "sim")

print(f'Tienes acesso ao desconto vip?: {es_elefible_para_el_desconto}')
