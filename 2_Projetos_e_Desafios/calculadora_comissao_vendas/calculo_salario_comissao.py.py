print("*** Calculadora de Comissão de vendas ***")
"""
VOÇÊ PRECISA CALCULAR O SALÁRIO FINAL DE UM VENDEDOR. O SALÁRIO É COMPOSTO POR UMA
PARTE FIXA MAIS UMA COMISSÃO, NO ENTANTO, SÓ É PAGA SE O VENDEDOR ATINGIR A VENDAS.
    AS REGRAS:
        1º O SALARIO FINAL É A SOMA DO salario_base mais o valor_da_comissao.
        2º A COMISSÃO SÓ É CALCULADA SE O  total_vendas FOR MAIOR OU IGUAL À meta_de_vendas.SE A META NÃO FOR ATENDIDA, A COMISSÃO É ZERO.
    SEU DESAFIO:
        1º CRIE AS VARIÁVEIS:
            1º  salario_base = 1500
            2º  total_vendas = 25000
            3º  meta_de_vendas = 20000
            4º  percentual_comissao = 0.05
        2º CALCULE O SALÁRIO FINAL EM ETAPAS:
            1º  CRIE UMA VARIÁVEL BOOLEANA CHAMADA atingiu_meta que verifica se o total_vendas é maior ou igual à meta_de_vendas.
            2º  CALCULE O valor_da_comissao. AQUI ESTÁ O TRUQUE: MULTIPLIQUE O VALOR TOTAL DA COMISSÃO total_vendas * percentual_comissao PELA SUA VARIÁVEL antiguiu_meta.(lembre-se:)
                 em cálculos, true se comporta como 1 e false como 0
            3º CALCULE O salario_final SOMANDO O salario_base e o valor_da_comissao que voçê avabou de calcular.
        3º imprima o resultado:
            1º "O salário final do vendedor é: R$[valor]"
"""
salario_base = 1500
total_vendas = 25000
meta_de_vendas = 20000
percentual_comissao = 0.05

atinguiu_meta = (total_vendas >= meta_de_vendas)
valor_da_comissao = (total_vendas * percentual_comissao) * atinguiu_meta
salario_final = salario_base + valor_da_comissao
print(f"O salário final do vendedor é: R${salario_final}")