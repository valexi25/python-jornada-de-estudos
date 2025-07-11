# Desafio: Verificador de Acesso a Evento

Este script simula um sistema de controle de entrada de um evento, aplicando um conjunto de regras de acesso que incluem condições de elegibilidade e uma restrição final.

## 🎯 Objetivo

O objetivo deste desafio é construir uma expressão booleana final que encapsula múltiplas regras de negócio, demonstrando o uso correto de parênteses para agrupar condições e a aplicação de uma restrição com o operador `not`.

## ⚙️ Regras de Acesso

Uma pessoa pode entrar no evento se a **condição de entrada** for verdadeira **E** se ela **NÃO** estiver na lista de restrição.

-   **Condição de Entrada (pelo menos uma das duas abaixo):**
    -   A pessoa tem 18 anos ou mais **E** possui um convite.
    *OU*
    -   A pessoa é uma convidada VIP.

**E**

-   **Restrição Final (deve ser falsa):**
    -   A pessoa **NÃO** pode estar na lista negra.

## 🚀 Como Executar

Execute o script diretamente para ver o resultado da verificação com os dados da pessoa pré-definidos no código.