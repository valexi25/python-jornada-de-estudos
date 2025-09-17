# Projeto: Mundo PC com Programação Orientada a Objetos

Este projeto simula a criação e gestão de ordens de computadores, aplicando conceitos avançados de Programação Orientada a Objetos (POO) em Python.

## 🎯 Objetivo

O objetivo é demonstrar a aplicação de **Composição** e **Herança** para modelar um sistema complexo. Diferente de projetos anteriores, este utiliza múltiplos arquivos para promover a modularidade e a organização do código, uma prática comum em projetos de software reais.

## ⚙️ Conceitos de POO Aplicados

-   **Composição**: A classe `Computadora` é composta por instâncias das classes `Monitor`, `Teclado` e `Raton`. A classe `Orden` é composta por uma lista de `Computadoras`.
-   **Herança**: As classes `Raton` e `Teclado` herdam da classe base `DispositivoEntrada`.
-   **Encapsulamento**: Atributos e métodos são agrupados dentro de classes que representam entidades lógicas.
-   **Modularidade**: Cada classe é definida em seu próprio arquivo, tornando o projeto mais fácil de manter e entender.

## 🚀 Como Executar

1.  Certifique-se de que todos os arquivos `.py` estejam na mesma pasta.
2.  Execute o arquivo principal da aplicação no seu terminal:
    ```bash
    python mundo_pc_app.py
    ```
3.  O script irá criar instâncias de vários componentes, montar computadores, adicioná-los a uma ordem e imprimir os detalhes.