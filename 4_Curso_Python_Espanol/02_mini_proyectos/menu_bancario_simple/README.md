# Mini Proyecto: Menú de Sistema Bancario Simple

Este script simula la opción de salida de un menú de sistema bancario, utilizando el operador lógico `not` para controlar el flujo.

## 🎯 Objetivo

El objetivo de este proyecto es demostrar cómo invertir una condición booleana con el operador `not` para tomar una decisión en un programa.

## ⚙️ Funcionalidad

El programa le pregunta al usuario si desea salir del sistema.
- Si el usuario responde algo diferente a "si", la condición `salir_sistema` es `False`, y `not salir_sistema` se convierte en `True`, por lo que el programa imprime "Continuamos dentro del sistema".
- Si el usuario responde "si", la condición `salir_sistema` es `True`, y `not salir_sistema` se convierte en `False`, por lo que el programa imprime "Salimos del sistema".

## 🚀 Cómo Ejecutar

1. Navega a la carpeta del proyecto en tu terminal.
2. Ejecuta el script con el comando:
   ```bash
   python control_de_salida.py