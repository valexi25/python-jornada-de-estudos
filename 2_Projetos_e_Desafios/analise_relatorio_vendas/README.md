# 🚀 Automação: Análise e Envio de Relatório de Vendas

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

Este projeto automatiza um fluxo de trabalho de análise de negócios: ele lê um relatório de vendas em formato CSV, calcula os principais indicadores de performance (faturamento e ticket médio) e envia um resumo por e-mail automaticamente via Outlook.

## 🎯 O Problema Resolvido

Analisar relatórios diários e comunicar os resultados para a equipe são tarefas essenciais, mas repetitivas. Esta ferramenta automatiza completamente esse processo, garantindo que os dados sejam processados e distribuídos de forma rápida e sem erros.

## ✨ Funcionalidades

-   **Análise de Dados:** Utiliza a biblioteca Pandas para ler um arquivo CSV, calcular o faturamento total e o ticket médio das vendas.
-   **Formatação de Relatório:** Cria um corpo de e-mail em HTML formatado, apresentando os dados de forma clara e profissional.
-   **Automação de E-mail:** Conecta-se diretamente com o aplicativo Outlook instalado no computador para criar e enviar o e-mail de relatório, incluindo o anexo do arquivo de vendas.

## 🛠️ Tecnologias Utilizadas

-   Python 3
-   **Pandas**: Para a leitura e análise dos dados do arquivo CSV.
-   **os**: Módulo nativo para interagir com o sistema de arquivos.
-   **pywin32**: Para a automação e integração com aplicações Windows, especificamente o Microsoft Outlook.

## ⚙️ Instalação

Para executar este projeto, você precisa instalar as bibliotecas necessárias. Abra seu terminal e rode o comando:
```bash
pip install pandas openpyxl pywin32

## 🚀 Como Usar

1.  Clone este repositório.
2.  Instale as dependências com o comando `pip` acima.
3.  Coloque o seu arquivo de vendas (ex: `Vendas.csv`) na mesma pasta que o script `main.py`.
4.  Abra o script `main.py` e altere o e-mail do destinatário na linha `email.To = "destinatario@email.com"`.
5.  Execute o script principal no seu terminal:
    ```bash
    python main.py
    ```
6.  O script irá processar o arquivo, e um e-mail com o resumo e o relatório em anexo será enviado automaticamente pelo seu Outlook.