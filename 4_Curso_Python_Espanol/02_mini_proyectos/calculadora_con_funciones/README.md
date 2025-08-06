# Mini Proyecto: Calculadora con Funciones

Este es un script de Python que implementa una calculadora básica de cuatro operaciones, estructurada con funciones y un menú interactivo.

## 🎯 Objetivo

El objetivo de este proyecto es practicar la **modularización del código** a través de la definición de funciones. Cada operación matemática es encapsulada en su propia función, y un loop `while` gestiona el flujo principal del programa.

## ⚙️ Funcionalidades

-   **Cuatro Operaciones:** Soporta suma, resta, multiplicación y división.
-   **Menú Interactivo:** Utiliza un ciclo `while` para permitir al usuario realizar múltiples cálculos sin tener que reiniciar el script.
-   **Código Modular:** Cada operación (sumar, restar, etc.) está definida en su propia función, promoviendo un código limpio y reutilizable.
-   **Manejo de Errores:** Utiliza un bloque `try/except` para gestionar entradas no numéricas y una validación específica para evitar la división por cero.

## 🚀 Cómo Usar

1.  Ejecuta el script en tu terminal:
    ```bash
    python calculadora.py
    ```
2.  Elige una opción del menú (1-5).
3.  Ingresa los números solicitados.
4.  El programa mostrará el resultado y volverá al menú principal.