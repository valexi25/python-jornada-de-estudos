# Desafio: Calculadora de Pontuação de Jogo

Este script calcula a pontuação final de um jogador em um game, aplicando uma fórmula específica que exige um controle rigoroso da ordem das operações.

## 🎯 Objetivo

O objetivo deste desafio é praticar o uso de parênteses `()` para forçar uma ordem de precedência específica em operações aritméticas, combinando soma, multiplicação, exponenciação e subtração.

## ⚙️ A Fórmula de Pontuação

A pontuação final é calculada seguindo exatamente esta ordem:
1.  Primeiro, calcula-se os pontos das moedas (`moedas_coletadas * multiplicador_moeda`).
2.  Soma-se o resultado aos `pontos_base`.
3.  Este novo total é elevado à potência do `bonus_estrela`.
4.  Finalmente, a `penalidade` é subtraída do resultado.

A expressão matemática é: `pontuacao_final = (pontos_base + (moedas_coletadas * multiplicador_moeda)) ** bonus_estrela - penalidade`

## 🚀 Como Executar

Execute o script diretamente para ver o resultado do cálculo com os valores pré-definidos.