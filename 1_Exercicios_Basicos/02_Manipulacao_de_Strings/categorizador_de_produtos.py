print("*** Organizador de Productos ***")
"""
  Códigos que començam com "FR" são Frutas.
  Códigos que començam com "LG" são Legumes.
  Códigos que començam com "CR"  são Carnes.
"""
codigo_producto = "LG-003"
categoria = ""


if codigo_producto.startswith("FR"):
    categoria = "Fruta"
elif codigo_producto.startswith("LG"):
    categoria = "Legumes"
elif codigo_producto.startswith("CR"):
    categoria = "Carne"
else:
    categoria = "Diversos"

print(f"O codigo {codigo_producto} pertence à categoria: {categoria} ")