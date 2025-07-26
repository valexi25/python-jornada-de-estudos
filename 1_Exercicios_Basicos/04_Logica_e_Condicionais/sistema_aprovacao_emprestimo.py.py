print("*** Sistema de Aprovação de Empréstimo ***")
"""
Regras para Aprocação:
    situação A: Salario mensal é de R$ 5.000 ou mais E o score de crédito pe de 700 ou mais.
    situação B: O salário mensal é de R$ 3.000 ou mais E o score de 800 ou mais E a idade é menor que 60 anos.
"""
salario_mensal = 4000.00
score_credito = 800
idade = 65
if ((salario_mensal >= 5000.00) and (score_credito >= 700)) or (((salario_mensal >= 3000.00)and(score_credito >= 800))and(idade <=60)) :
    print("Emprestimo Aprovado")
else:
    print("Emprestimo NEGADO")