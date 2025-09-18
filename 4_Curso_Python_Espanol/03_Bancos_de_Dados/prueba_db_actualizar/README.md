# Script para Atualizar Registros no Banco de Dados

Este script em Python demonstra como modificar múltiplos registros existentes em uma tabela do PostgreSQL de uma só vez.

## 🎯 Objetivo

O objetivo é praticar a execução do comando `UPDATE` do SQL, utilizando o método `cursor.executemany()` da biblioteca `psycopg2` para aplicar a mesma operação a uma lista de dados de forma eficiente e segura.

## ⚙️ Funcionalidades

-   Conecta-se a um banco de dados PostgreSQL.
-   Define uma lista de tuplas, onde cada tupla contém os novos dados (`nome`, `apellido`, `email`) e o `id_persona` do registro a ser atualizado.
-   Executa um comando `UPDATE` parametrizado para cada item da lista.
-   Utiliza o atributo `cursor.rowcount` para informar quantos registros foram atualizados.

## ⚙️ Pré-requisitos

1.  **PostgreSQL**: Servidor PostgreSQL em execução.
2.  **Biblioteca `psycopg2`**: `pip install psycopg2-binary`
3.  **Tabela `persona`**: A tabela deve existir no banco de dados.

## 🚀 Como Executar

1.  Ajuste os dados de conexão no arquivo `atualizar_registros.py`.
2.  Execute o script no seu terminal:
    ```bash
    python atualizar_registros.py
    ```