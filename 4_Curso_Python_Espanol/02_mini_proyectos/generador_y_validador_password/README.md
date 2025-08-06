# Mini Proyecto: Generador y Validador de Contraseñas

Esta es una herramienta de línea de comandos en Python que permite a los usuarios generar contraseñas seguras y aleatorias, o validar la fortaleza de una contraseña existente.

## 🎯 Objetivo

El objetivo de este proyecto es practicar la manipulación de strings, el uso de funciones para modularizar el código y la implementación de una lógica de validación compleja para verificar múltiples criterios de seguridad en una contraseña.

## ⚙️ Funcionalidades

El programa ofrece un menú interactivo con dos opciones principales:
1.  **Crear Contraseña:** Genera una contraseña aleatoria de 12 caracteres que incluye letras mayúsculas, minúsculas, números y símbolos.
2.  **Validar Contraseña:** Solicita al usuario que ingrese una contraseña y la verifica contra las siguientes reglas:
    -   Debe tener al menos 8 caracteres.
    -   Debe contener al menos una letra mayúscula.
    -   Debe contener al menos una letra minúscula.
    -   Debe contener al menos un número.
    -   Debe contener al menos un símbolo.

## 🚀 Cómo Usar

1.  Ejecuta el script en tu terminal:
    ```bash
    python password_tool.py
    ```
2.  Elige una opción del menú (1 o 2).
3.  Sigue las instrucciones en pantalla.