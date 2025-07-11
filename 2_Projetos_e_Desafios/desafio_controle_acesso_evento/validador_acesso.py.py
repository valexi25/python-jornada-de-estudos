print("*** Verificador de Acesso a Evento ***")
""""    
    VOCÊ ESTA PROGRAMANDO O SISTEMA DE CONTROLE DE ENTRADA PARA UM EVENTO. AS REGRAS DE ACESSO SÃO AS SEGUINTES:
        UMA PESSOA PODE ENTRAR SE:
            º ela for maior de 18 anos e tiver um convite
            º ela for una convidada vip
        PORÉM, HÁ UNA RESTRINÇÃO FINAL: NINGÉM QUE ESTEJA NA LISTA "NEGRA" pode entrar, não importa as outras condições.

        DESAFIO:
       1 CRIAR AS SEGUINTES VARIÁVEIS DE ESTADO PARA UMA PESSOA:
            º idade = 25
            º tem_convite = true
            º eh_vip = false
            º esta_na_lista_negra = false
        2 CRIE A LÓGICA DE ACESSO:
            º crieuma variável booleana chamada pode_entrar.
            º esta variável deve ser True apenas se as regras de acesso forem satisfeitas, e false caso contrário.
            º use parênteses () para agrupar as condições corretamente. a expressão final deve ser algo como: (condicao_principal)
        3 IMPRIMA O RESULTADO:
            º "A pessoa pode entrar no evento? [resultado]" 
"""
idade = 25
tem_convite = True
eh_vip = True
esta_na_lista_negra = True

condicoes_para_entrar = (idade > 18 and tem_convite) or eh_vip

pode_entrar = condicoes_para_entrar and not esta_na_lista_negra

print(f"A pessoa pode entrar no evento? {pode_entrar}")