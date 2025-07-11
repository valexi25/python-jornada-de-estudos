# Desafio: Verificador de Configuração de Servidor

Este script avalia um conjunto de variáveis que representam a configuração de um servidor para determinar se ele está estável e pronto para entrar em produção.

## 🎯 Objetivo

O objetivo deste desafio é construir uma expressão booleana complexa que combina múltiplas sub-condições com os operadores `and` e `or`, utilizando parênteses para garantir a precedência correta das operações lógicas.

## ⚙️ Regras para Prontidão

Para ser considerado "Pronto para Produção", o servidor deve atender à **Condição Essencial** e a, pelo menos, uma das **Opções de Suporte**.

-   **Condição Essencial (Obrigatória):**
    -   O `sistema_operacional` deve ser "Linux" **E** a `memoria_ram` deve ser de 16GB ou mais.

**E**

-   **Opções de Suporte (Pelo menos uma das duas):**
    -   **Opção de Redundância:** O `tipo_de_armazenamento` é "SSD" **E** o `backup_automatico` está ativo.
    *OU*
    -   **Opção de Desempenho:** O `cores_cpu` é 8 ou mais **E** o `servico_firewall` está ativo.

## 🚀 Como Executar

Execute o script diretamente. Ele usará os valores pré-definidos para as variáveis de configuração e imprimirá o resultado da avaliação.