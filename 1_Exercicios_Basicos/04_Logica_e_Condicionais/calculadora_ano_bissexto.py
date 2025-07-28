print("*** Calculadora de Ano Bissexto **")
"""
    Regras do ano bissexto:
    É divisível por 4.
    Amenos que ele tambem seja divisivel por 100.
    A Não ser que ele seja divisivel por 400
"""
ano = 2024

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 ==0):
    print(f"O ano {ano} é um ano Bissexto")
else:
     print(f"O ano {ano} nao é um ano bissexto")