# Projeto: Conexão com Banco de Dados PostgreSQL

Este projeto demonstra como conectar uma aplicação Python a um banco de dados PostgreSQL para executar consultas de leitura de dados (`SELECT`).

## 🎯 Objetivo

O objetivo é praticar as etapas fundamentais da interação com um banco de dados:
-   Estabelecer uma conexão usando a biblioteca `psycopg2`.
-   Executar uma consulta SQL de forma segura, utilizando **consultas parametrizadas** para prevenir injeção de SQL.
-   Gerenciar a conexão e o cursor de forma segura com blocos `with`.
-   Tratar possíveis erros com `try-except-finally`.

## ⚙️ Pré-requisitos

1.  **PostgreSQL**: É necessário ter um servidor PostgreSQL em execução.
2.  **Biblioteca `psycopg2`**: Instale a biblioteca com o seguinte comando:
    ```bash
    pip install psycopg2-binary
    ```
3.  **Tabela no Banco de Dados**: O script espera que exista uma tabela `persona` no banco de dados. Você pode criá-la com o seguinte comando SQL:
    ```sql
    CREATE TABLE persona (
        id_persona SERIAL PRIMARY KEY,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        email VARCHAR(100)
    );
    ```

## 🚀 Como Executar

1.  Ajuste os dados de conexão (usuário, senha, host, etc.) no arquivo `conectar_e_consultar.py`.
2.  Execute o script no seu terminal:
    ```bash
    python conectar_e_consultar.py
    ```
3.  O programa solicitará os IDs das pessoas que você deseja buscar, separados por vírgula.