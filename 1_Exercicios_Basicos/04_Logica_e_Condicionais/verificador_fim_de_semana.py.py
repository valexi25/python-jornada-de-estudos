print("*** É Fim de Semana ***")
"""
Objetivo: Criar um programa que decide se um dia da semana é parte do fim de semana.
Instruções:
    Criar uma variávle chamada é fim de semana.
    Escreva uma estrutura If/else.
    A condição do if deve verificar se a variável é igual ao dia da semana.
    Se a condição e verdadeira, o programa deve imprimir: É fim de semana! Hora de descansar.
    Caso cotrário, deve imprimir: É dia de semana. foco no trabalho/estudo!
"""
fim_semana = "lunes"

if fim_semana == "sabado" or fim_semana == "domingo":
    print(f"{fim_semana} É fim de semana! Hora de descansar")
else:
    print(f"{fim_semana} É dia de semana. Foco no trabalho/estudo!")
