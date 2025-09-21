# Projeto: Gerenciador de Usuários com Padrão DAO

Esta é uma aplicação de console completa para gerenciar um cadastro de usuários, implementada em Python e utilizando uma arquitetura em camadas com o padrão de design Data Access Object (DAO).

## 🎯 Objetivo

O objetivo é construir uma aplicação robusta que separa as responsabilidades do código:
-   **Camada de Apresentação**: Um menu interativo para o usuário.
-   **Camada de Dados**: Uma camada de acesso a dados (DAO) que encapsula toda a lógica SQL.
-   **Camada de Domínio**: Classes que representam as entidades do negócio (ex: `Usuario`).

## ⚙️ Conceitos Aplicados

-   **Padrão DAO**: A classe `UsuarioDAO` centraliza todos os métodos para interagir com a tabela `usuario`.
-   **Connection Pooling**: A classe `Conexion` gerencia um "pool" de conexões de banco de dados para reutilizá-las de forma eficiente.
-   **Gerenciador de Contexto (`with`)**: A classe `CursorDelPool` gerencia automaticamente a obtenção e liberação de recursos do banco de dados, além de transações.
-   **Logging**: Um sistema de log registra as operações em um arquivo (`capa_datos.log`) e no console para facilitar a depuração.

## ⚙️ Pré-requisitos

1.  **PostgreSQL**: É necessário ter um servidor PostgreSQL em execução.
2.  **Biblioteca `psycopg2`**: Instale com `pip install psycopg2-binary`.
3.  **Tabela `usuario`**: A tabela deve existir no banco. Use o seguinte SQL para criá-la:
    ```sql
    CREATE TABLE usuario (
        id_usuario SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL
    );
    ```

## 🚀 Como Executar

1.  Ajuste as credenciais de conexão no arquivo `conexion.py`.
2.  Execute o arquivo do menu principal:
    ```bash
    python menu_app_usuario.py
    ```
3.  Siga as opções do menu para listar, adicionar, modificar ou excluir usuários.