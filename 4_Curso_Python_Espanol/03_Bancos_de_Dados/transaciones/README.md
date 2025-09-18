# Gerenciamento de Transações com Psycopg2

Este script demonstra como agrupar múltiplas operações de banco de dados em uma única **transação** em Python.

## 🎯 Objetivo

O objetivo é praticar o gerenciamento de transações para garantir a **integridade dos dados**. Uma transação é uma sequência de operações que são executadas como uma única unidade lógica de trabalho. A regra é "tudo ou nada": ou todas as operações são concluídas com sucesso (`commit`), ou, se ocorrer um erro, todas as operações anteriores são desfeitas (`rollback`).

## ⚙️ Funcionalidades

-   **Bloco `with`**: O script utiliza o gerenciador de contexto `with conexion:` da biblioteca `psycopg2`. Esta é a forma recomendada de lidar com transações, pois ele automaticamente:
    -   Executa um `commit` se o bloco de código for concluído sem erros.
    -   Executa um `rollback` se qualquer exceção ocorrer dentro do bloco.
-   **Múltiplas Operações**: O script tenta executar um `INSERT` e um `UPDATE` dentro da mesma transação.
-   **Tratamento de Erros**: Um bloco `try...except` captura qualquer erro que possa ocorrer, garantindo que o programa não pare abruptamente.

## 🚀 Como Executar

1.  Ajuste os dados de conexão no arquivo `gerenciamento_de_transacoes.py`.
2.  Execute o script no seu terminal:
    ```bash
    python gerenciamento_de_transacoes.py
    ```