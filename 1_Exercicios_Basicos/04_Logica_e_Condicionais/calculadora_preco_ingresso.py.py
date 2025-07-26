print("*** Calculo da Media ***")
"""
    Regras de preço:
        preço normal:$ 30,00
        menores de 18 e maiores de 65 pagam mnedia-entrada(R$15,00)
    para quem tem entre 18 e 65 anos:
        Se for estudante, o preço é R$ 20,00.
        Se não for estudante,paga o preço normal (R$ 30,00)
    
"""
idade = 40
eh_estudante = False

if (18 > idade) or (idade > 65):
    print("Preço do Ingreso: R$ 15,00")
else:
    if eh_estudante == True:
        print("Preço do ingresse: R$ 20,00")
    else:
        print("Preço da entrada R$ 30,00")
