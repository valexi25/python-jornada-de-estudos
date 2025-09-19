# Projeto: Camada de Acesso a Dados (DAO) com PostgreSQL

Este projeto implementa o padrão de design **Data Access Object (DAO)** em Python para gerenciar as operações de um banco de dados PostgreSQL de forma organizada e escalável.

## 🎯 Objetivo

O objetivo é separar a lógica de acesso a dados da lógica de negócios. Em vez de escrever consultas SQL diretamente no código da aplicação, criamos uma camada de abstração (`PersonaDAO`) que lida com todas as operações CRUD (Criar, Ler, Atualizar, Deletar).

## ⚙️ Conceitos Aplicados

-   **Padrão DAO**: A classe `PersonaDAO` centraliza todos os métodos para interagir com a tabela `persona` (`selecionar`, `insertar`, `actualizar`, `eliminar`).
-   **Connection Pooling**: A classe `Conexion` gerencia um "pool" de conexões de banco de dados para reutilizá-las, o que é muito mais eficiente do que abrir e fechar uma nova conexão para cada operação.
-   **Gerenciador de Contexto (`with`)**: A classe `CursorDelPool` usa os métodos `__enter__` e `__exit__` para gerenciar automaticamente a obtenção e liberação de conexões e cursores do pool, além de cuidar do `commit` e `rollback`.
-   **Logging**: O módulo `logger_base` configura um sistema de log que registra as operações em um arquivo (`capa_datos.log`) e no console, facilitando a depuração.
-   **Classes de Domínio**: A classe `Persona` representa a entidade do nosso negócio, funcionando como um objeto para transportar dados.

## 🚀 Como Executar

1.  Certifique-se de que todos os arquivos `.py` estejam na mesma pasta.
2.  Ajuste as credenciais de conexão no arquivo `conexion.py`.
3.  Execute o arquivo `persona_dao.py` para ver os testes de inserção, atualização, exclusão e seleção em ação:
    ```bash
    python persona_dao.py
    ```
4.  Verifique o arquivo `capa_datos.log` que será gerado para ver o registro detalhado de todas as operações.