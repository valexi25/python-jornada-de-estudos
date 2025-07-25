# Mini Proyecto: Sistema de Autenticación

Este proyecto explora dos enfoques para crear un sistema de login simple en Python, demonstrando diferentes níveis de feedback para o usuário.

## 🎯 Objetivo

El objetivo de este proyecto es practicar la lógica condicional para validar datos. Se exploram duas implementações:
-   Una validación booleana simple.
-   Un sistema de respuestas múltiples y detalladas.

---
## ⚙️ Versiones del Script

Este repositório contém duas versões do validador:

### Versión 1: `autenticacion_basica.py`

Este script realiza una validación directa. Compara el usuario y la contraseña ingresados con los valores correctos y devuelve un único resultado booleano: `True` si todo es correcto, `False` en caso contrario.

### Versión 2: `autenticacion_multicaso.py`

Esta versión avanzada expande la lógica para proporcionar un feedback más detallado al usuario. En lugar de un simple `True`/`False`, el script utiliza uma estrutura `if/elif/else` para identificar y reportar específicamente si el error está en el nombre de usuario, en la contraseña, o en ambos.

---
## 🚀 Cómo Ejecutar

1.  Navega a la carpeta del proyecto en tu terminal.
2.  Ejecuta cualquiera de las dos versiones para comparar su comportamiento:

    ```bash
    # Para ejecutar la versión básica (True/False)
    python autenticacion_basica.py
    ```
    ```bash
    # Para ejecutar la versión con múltiples respuestas
    python autenticacion_multicaso.py
    ```