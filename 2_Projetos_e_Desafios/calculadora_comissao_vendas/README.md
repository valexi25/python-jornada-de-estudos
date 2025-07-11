# Desafio: Calculadora de Comissão de Vendas

Este script calcula o salário final de um vendedor, que é composto por um salário base mais uma comissão variável, paga apenas se uma meta de vendas for atingida.

## 🎯 Objetivo

O objetivo deste desafio é demonstrar uma forma inteligente de aplicar lógica condicional sem usar uma estrutura `if/else` explícita. O projeto utiliza o fato de que, em cálculos aritméticos, o valor Booleano `True` se comporta como o número `1` e `False` se comporta como `0`.

## ⚙️ Lógica do Cálculo

1.  Uma variável booleana `atingiu_meta` é criada para verificar se o `total_vendas` é maior ou igual à `meta_de_vendas`.
2.  O `valor_da_comissao` é calculado multiplicando-se o valor total da comissão pela variável `atingiu_meta`.
    - Se `atingiu_meta` for `True` (1), a comissão é calculada normalmente.
    - Se `atingiu_meta` for `False` (0), o resultado da multiplicação é zero, zerando a comissão.
3.  O `salario_final` é a soma do `salario_base` com o `valor_da_comissao` resultante.

## 🚀 Como Executar

Execute o script diretamente para ver o resultado do cálculo com os valores pré-definidos.