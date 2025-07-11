# Desafio: Conversor de Segundos

Este script converte uma quantidade total de segundos para o formato de horas, minutos e segundos.

## 🎯 Objetivo

O objetivo deste desafio é praticar a lógica de conversão de unidades de tempo, utilizando intensivamente os operadores de divisão inteira (`//`) e módulo (`%`) para decompor um valor total em suas partes constituintes.

## ⚙️ Lógica da Conversão

O script segue os seguintes passos:
1.  Calcula quantas horas completas cabem no total de segundos (1 hora = 3600 segundos).
2.  Usa o operador módulo para encontrar os segundos que "sobraram" após a extração das horas.
3.  Usa esses segundos restantes para calcular quantos minutos completos eles formam (1 minuto = 60 segundos).
4.  Finalmente, usa o módulo novamente para encontrar os segundos finais que não formaram um minuto completo.

## 🚀 Como Executar

Execute o script diretamente para ver o resultado da conversão do valor pré-definido no código.