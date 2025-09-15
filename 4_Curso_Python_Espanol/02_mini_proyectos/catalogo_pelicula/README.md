# Mini Proyecto: Catálogo de Películas

Este es un script en Python que implementa un gestor de catálogo de películas, permitiendo a los usuarios agregar, listar y eliminar películas de un archivo de texto.

## 🎯 Objetivo

El objetivo principal de este proyecto es aplicar los principios de la **Programación Orientada a Objetos (POO)** en Python. Se practica la creación de clases, la gestión de objetos y la interacción con archivos para la persistencia de datos.

## ⚙️ Funcionalidades

-   **Agregar Película:** Permite al usuario añadir una nueva película al catálogo. La información se guarda en un archivo `peliculas.txt`.
-   **Listar Películas:** Lee el archivo `peliculas.txt` y muestra todas las películas guardadas.
-   **Eliminar Catálogo:** Borra el archivo `peliculas.txt`, eliminando todas las películas guardadas.
-   **Menú Interactivo:** Un ciclo `while` mantiene el programa en ejecución hasta que el usuario decide salir.

## 🛠️ Estructura del Código (POO)

El proyecto está organizado en dos clases principales para separar responsabilidades:
-   **`Pelicula`**: Representa una sola película, conteniendo su nombre como un atributo.
-   **`CatalogoPeliculas`**: Actúa como una clase de servicio que contiene la lógica para manejar el archivo del catálogo (agregar, listar, eliminar).

## 🚀 Cómo Usar

1.  Ejecuta el script en tu terminal:
    ```bash
    python main.py
    ```
2.  Elige una opción del menú (1-4) y sigue las instrucciones en pantalla.