# Projeto: CRUD Básico com MySQL

Este projeto consiste em um conjunto de scripts Python que demonstram as quatro operações fundamentais de um banco de dados (CRUD: Create, Read, Update, Delete) utilizando o conector oficial do MySQL.

## 🎯 Objetivo

O objetivo é praticar cada uma das operações SQL essenciais de forma isolada, conectando Python a um banco de dados MySQL.

## ⚙️ Scripts

-   **`insertar.py`**: Insere um novo registro na tabela `personas`.
-   **`selecionar.py`**: Seleciona e exibe todos os registros da tabela.
-   **`actualizar.py`**: Atualiza um registro existente com base em seu ID.
-   **`eliminar.py`**: Deleta um registro existente com base em seu ID.

## ⚙️ Pré-requisitos

1.  **MySQL**: É necessário ter um servidor MySQL em execução.
2.  **Biblioteca `mysql-connector-python`**: Instale a biblioteca com o seguinte comando:
    ```bash
    pip install mysql-connector-python
    ```
3.  **Tabela `personas`**: O banco de dados deve ter uma tabela chamada `personas`. Use o seguinte comando SQL para criá-la:
    ```sql
    CREATE TABLE personas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        edad INT
    );
    ```

## 🚀 Como Executar

1.  Ajuste os dados de conexão (usuário, senha, etc.) em cada um dos scripts.
2.  Execute o script desejado no seu terminal. Por exemplo:
    ```bash
    python selecionar.py
    ```