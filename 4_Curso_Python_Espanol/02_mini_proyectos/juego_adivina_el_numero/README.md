# Mini Proyecto: Juego de Adivinar el Número

Este es un juego clásico de adivinanzas implementado en Python, donde el jugador debe adivinar un número secreto generado por la computadora.

## 🎯 Objetivo

El objetivo de este proyecto es practicar la combinación de varias estructuras fundamentales de programación:
- Generación de números aleatorios con el módulo `random`.
- Creación de un bucle de juego con `while`.
- Uso de lógica condicional `if/elif/else` para guiar al jugador.
- Gestión de un estado (intentos restantes).

## ⚙️ Funcionalidades

-   **Número Aleatorio:** Al iniciar, el programa elige un número secreto entre 1 y 100.
-   **Sistema de Pistas:** Después de cada intento, el juego informa al jugador si su número es más alto o más bajo que el número secreto.
-   **Límite de Intentos:** El jugador tiene un máximo de 10 intentos para adivinar el número.
-   **Resultados Claros:** El programa informa si el jugador ha ganado (adivinado el número) o perdido (se han acabado los intentos).

## 🚀 Cómo Jugar

1.  Ejecuta el script en tu terminal:
    ```bash
    python juego.py
    ```
2.  Ingresa un número entre 1 y 100 cuando se te solicite.
3.  Sigue las pistas para intentar adivinar el número en menos de 10 intentos.