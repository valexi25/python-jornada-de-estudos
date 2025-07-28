print("*** Calculadora de Imposto de Renda Simplificada ****")
"""
    Sálario até R$ 2000,00: isento
    Sálario de R$ 2000,01 a R$ 3000,00: alíquota de 8%
    Sálario de 3000,01 a R$ 4500,00:alíquota de 18%
    Sálario de acima de 4500,00: alíquota de 28%
"""
salario = 2000.00

if 2000.01 <= salario <= 3000.00:
    print(f"Seu salario é de R${salario} Seu imposto é de R${salario *0.08:.2f}")
elif 3000.01 <= salario <= 4500.00:
    print(f"Seu salario é de R${salario} Seu imposto é de R${salario * 0.18:.2f}")
elif salario >= 4500.01:
    print(f"Seu salario é de R${salario} Seu imposto é de R${salario * 0.28:.2f}")
else:
    print(f"Seu salario é de {salario:.2f} Você esta insento de inposto")