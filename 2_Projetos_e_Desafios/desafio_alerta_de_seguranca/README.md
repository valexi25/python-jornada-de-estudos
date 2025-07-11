# Desafio: Sistema de Alerta de Segurança

Este script implementa a lógica de um sistema de segurança complexo para determinar se um "Alerta Máximo" deve ser disparado.

## 🎯 Objetivo

O objetivo deste desafio é traduzir um conjunto de regras de negócio complexas em uma única expressão lógica booleana, utilizando operadores `and` e `or` e agrupando condições com parênteses para garantir a ordem de precedência correta.

## ⚙️ Regras para o Alerta Máximo

O alerta é disparado (`True`) se **qualquer uma** das três situações a seguir for verdadeira:

-   **Situação A:** O sensor de movimento principal está ativo **E** o sistema está armado **E** (a janela da sala foi aberta **OU** a porta dos fundos foi aberta).

*OU*

-   **Situação B:** O sensor de pressão do cofre foi ativado **E** o horário é fora do expediente.

*OU*

-   **Situação C:** O botão de pânico foi pressionado.

O script avalia o estado de várias variáveis booleanas para determinar o resultado final.

## 🚀 Como Executar

Execute o script diretamente. Ele usará os valores pré-definidos no código para calcular e exibir o status do alerta.