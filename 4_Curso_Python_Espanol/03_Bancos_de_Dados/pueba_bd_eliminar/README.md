# Script para Deletar Registros no Banco de Dados

Este script em Python demonstra como remover registros de uma tabela em um banco de dados PostgreSQL de forma segura.

## 🎯 Objetivo

O objetivo principal é praticar a execução do comando `DELETE FROM` do SQL através do Python, utilizando a biblioteca `psycopg2`. O foco é garantir que a operação seja feita de forma segura, usando **consultas parametrizadas** para evitar injeção de SQL.

## ⚙️ Funcionalidades

-   Conecta-se a um banco de dados PostgreSQL.
-   Solicita ao usuário que forneça um ou mais IDs dos registros a serem deletados.
-   Executa um comando `DELETE` de forma segura, passando os IDs como parâmetros.
-   Utiliza o atributo `cursor.rowcount` para informar quantos registros foram efetivamente removidos do banco.
-   Inclui tratamento de erros (`try-except`) e garante que a conexão com o banco seja sempre fechada (`finally`).

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

1.  No arquivo `deletar_registros.py`, substitua os dados de conexão (`sua-senha`, `seu-host`, etc.) pelos seus dados reais.
2.  Execute o script no seu terminal:
    ```bash
    python deletar_registros.py
    ```
3.  O programa solicitará os IDs que você deseja deletar, separados por vírgula.