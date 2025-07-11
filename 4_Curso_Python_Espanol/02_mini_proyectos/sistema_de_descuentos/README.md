# Mini Proyecto: Sistema de Descuentos para Tienda Online

Este script calcula el descuento aplicable a una compra basándose en el monto total y si el cliente es miembro de la tienda.

## 🎯 Objetivo

El objetivo de este proyecto es practicar la creación de una estructura de control `if/elif/else` compleja, que utiliza operadores lógicos `and` y `or` para evaluar múltiples condiciones y determinar el resultado correcto.

## ⚙️ Lógica de Descuentos

El programa aplica las siguientes reglas:
- **10% de descuento:** Si el monto de la compra es mayor o igual a $1000 **Y** el cliente es miembro.
- **5% de descuento:** Si el cliente es miembro (y la compra es menor a $1000).
- **0% de descuento:** Si no se cumple ninguna de las condiciones anteriores.

## 🚀 Cómo Ejecutar

1.  Navega a la carpeta del proyecto en tu terminal.
2.  Ejecuta el script con el comando:
    ```bash
    python calculadora_descuentos.py
    ```