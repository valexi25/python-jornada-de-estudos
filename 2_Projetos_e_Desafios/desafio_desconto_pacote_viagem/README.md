# Desafio: Validação de Pacote de Viagem com Desconto

Este script implementa a lógica de negócio de uma agência de viagens para determinar se um cliente é elegível para um desconto especial em um pacote de viagem.

## 🎯 Objetivo

O objetivo deste desafio é construir uma expressão booleana complexa que combina múltiplos critérios e uma restrição final. É um exercício focado no uso correto de parênteses `()` para agrupar condições e garantir que os operadores `and`, `or` e `not` sejam aplicados na ordem correta.

## ⚙️ Regras para o Desconto

Um cliente recebe o desconto se a **condição de elegibilidade** for verdadeira **E** a **restrição** for falsa.

-   **Condição de Elegibilidade (pelo menos uma das duas abaixo):**
    -   O pacote é para 2 ou mais pessoas **E** a duração da viagem é de 5 ou mais dias.
    *OU*
    -   O cliente é um membro "Premium".

**E**

-   **Restrição (deve ser falsa):**
    -   A viagem **NÃO** pode ser durante um feriado nacional prolongado.

A estrutura lógica final é: `((criterio1_A AND criterio1_B) OR criterio2) AND (NOT restricao)`

## 🚀 Como Executar

Execute o script diretamente para ver o resultado da avaliação com os dados pré-definidos no código.