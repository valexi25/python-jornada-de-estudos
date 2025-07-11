# Desafio: Codificador Numérico

Este script implementa um algoritmo de codificação que transforma um número inteiro de 3 dígitos em um novo número, seguindo um conjunto de regras específicas.

## 🎯 Objetivo

O objetivo deste desafio é praticar a manipulação de números inteiros, utilizando operadores aritméticos como a divisão inteira (`//`) e o módulo (`%`) para decompor e recompor números, além de seguir um algoritmo passo a passo.

## ⚙️ O Algoritmo de Codificação

O processo de codificação segue 4 etapas:

1.  **Separação**: Um número de 3 dígitos (ex: 742) tem cada um de seus dígitos separado em uma variável individual.
    - `dígito1 = 7`, `dígito2 = 4`, `dígito3 = 2`

2.  **Transformação**: Uma regra matemática é aplicada a cada dígito: `novo_dígito = (dígito_original + 5) % 10`.
    - `novo_dígito1 = (7+5)%10 -> 2`
    - `novo_dígito2 = (4+5)%10 -> 9`
    - `novo_dígito3 = (2+5)%10 -> 7`

3.  **Troca**: A posição do primeiro e do terceiro dígito transformado são trocadas.
    - Antes: `2, 9, 7`
    - Depois: `7, 9, 2`

4.  **Recombinação**: Os novos dígitos são unidos para formar o número codificado final.
    - `número_codificado = 7*100 + 9*10 + 2 -> 792`

## 🚀 Como Executar

Execute o script diretamente para ver o resultado da codificação do número pré-definido no código.