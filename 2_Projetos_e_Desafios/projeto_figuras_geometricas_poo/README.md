# Projeto: Figuras Geométricas com Programação Orientada a Objetos (POO)

Este projeto demonstra a implementação de conceitos de Programação Orientada a Objetos em Python, como classes, herança e classes abstratas, para modelar figuras geométricas.

## 🎯 Objetivo

O objetivo principal é praticar e demonstrar o uso de **herança** e **polimorfismo**. O projeto cria uma estrutura onde classes específicas (`Cuadrado`, `Retangulo`) herdam de uma classe base abstrata (`FiguraGeometrica`), sendo forçadas a implementar seus próprios métodos de cálculo de área.

## ⚙️ Estrutura do Projeto

O projeto é dividido em múltiplos arquivos para promover a modularidade:
-   **`figura_geometrica.py`**: Define a classe base abstrata `FiguraGeometrica`, que serve como um "contrato" para todas as outras figuras.
-   **`color.py`**: Define a classe `Color`, que é usada como um atributo dentro das figuras.
-   **`cuadrado.py`**: Define a classe `Cuadrado`, que herda de `FiguraGeometrica` e implementa o cálculo de área específico para um quadrado.
-   **`retangulo.py`**: Define a classe `Retangulo`, que também herda de `FiguraGeometrica` e implementa o cálculo de área para um retângulo.
-   **`teste_figura_gemoetrica.py`**: É o script principal que importa as classes, cria objetos (instâncias) e testa a funcionalidade, demonstrando o polimorfismo em ação.

## 🚀 Como Executar

1.  Certifique-se de que todos os arquivos `.py` estejam na mesma pasta.
2.  Execute o arquivo de teste no seu terminal:
    ```bash
    python teste_figura_gemoetrica.py
    ```
3.  O script irá imprimir os detalhes e a área calculada para um quadrado e um retângulo.