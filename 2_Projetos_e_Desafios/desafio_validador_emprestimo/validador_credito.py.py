print("*** Validador de Empréstimo Bancário ***")
"""""
    VOCÊ PRECISA CRIAR UM SCRIPT QUE DETERMINE SE UM CLIENTE ESTÁ ELEGIVEL PARA UM EMPRÉSTIMO. AS REGRAS DO BANCO SÃO RIGIDAS E
    TODAS AS CONDIÇÕES A SEGUIR PRECISAM SER VERDADEIRAS.
        REGRAS PARA ELEGIBILIDADE:
             1º A RENDA MENSAL DEVE SER DE, NO MINIMO,R$ 3.000.
             2º O CLIENTE DEVE ESTAR NO EMPREGO ATUAL HÁ PELO MENOS 2 ANOS.
             3º O VALOR DO EMPRÉSTIMO SOLICITADO NÃO PODE SER MAIOR QUE 10 VEZES A RENDA MENSAL DO CLIENTE.
             4º O CLIENTE NÃO PODE TER NENHUM OUTRO ENPRÉSTIMO ATIVO NO BANCO.

        SEU DESAFIO:
            1º CRIAR AS VARIAVEIS PARA UM CLIENTE
                °1 renda_mensual = 4000
                º2 valor_emprestimo_solicitado = 30000
                º3 anos_no_emprego = 3
                º4 possui_emprestimo_ativo = false
            2º  CRIE UMA ÚNICA VARIÁVEL BOOLEANA   emprestimo_aprovado:
                º1 ESSA VARIÁVEL DEVE SER TRUE SOMENTE SE TODAS AS 4 REGRAS FOREM ATENDIDAS,E FALSE CASO CONTRÁRIO.
                º2 COMBINE OPERADORES ARITMÉTICOS, DE COMPARAÇÃO E LÓGICOS PARA FORMAR UMA ÚNICA EXPRESSÃO.
            3º  º3 "ANÁLISE DE CRÉDITO: EMPRÉSTIMO APROVADO?"
"""
renda_mensual = 4000
valor_emprestimo_solicitado = 30000
anos_no_emprego = 4
possui_emprestimo_ativo = False

criterio_aprovação = (renda_mensual >= 3000) and (anos_no_emprego >= 2) and (renda_mensual * 10 >= valor_emprestimo_solicitado)
emprestimo_aprovado = criterio_aprovação and not possui_emprestimo_ativo

print(f"Análisis de Crédito: {emprestimo_aprovado}")