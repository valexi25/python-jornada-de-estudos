print("**** Calculadora de Pontuação de Jogo ****")
# IMAGINE QUE VOCÊ ESTÁ PROGRAMANDO A PONTUAÇÃO FINLA DE UM JOGADOR EM UM GAME. A PONTUAÇÃO É CALCULADA COM BASE EM VÁRIAS AÇÕES É MUITO IMPORTANTE.
# SEU DESAFIO É CALCULAR A pontuacao_final COM BASE NAS SEGUINTES VARIÁVEIS E REGRAS:
# º1 variaveis iniciais 1º pontos_base = 1000, 2º moedas_coletadas = 25, 3º multiplicador_moeda = 5, 4º bonus_estrala = 2  (O BÔNUS ELEVA A PONTUAÇÃO À POTÊNCIA DO SEU VALOR), 5º penalidade = 300
# º2 CALCULE A PONTUAÇÃO FINAL SEGUINDO ESTA ORDEM ESPECIFICA: 1º SOME OS pontos_base COM TOTAL DE PONTOS DAS MOEDAS(que é moedas_coletadosa * multiplicador_moeda). 2º EM SEGUIDA, ELEVE ESSE RESULTADO À POTÊNCIA DO bonus_estrela (use o operador de exponeciação **). 3º POR FIM, SUBTRAIA O VALOR DA penalidade DO RESULTADO.
# º3 ARMAZENE O RESULTADO EM UMA VARIÁVEL CHAMADA pontuação_final. USE PARÊNTESES () PARA GARANTIR QUE A ORDEM DAS OPERAÇÕES (SOMA, DEPOIS POTÊNCIA, DEPOIS SUTRAÇÃO) SEJA SEGIDA CORRETAMENTE.
# º4 IMPRIMA O RESULTADO DE FORMA CLARA, COMO:"A pontuação final do jogador é: {resultado}";

pontos_base = 1000
moedas_coletadas = 25
multiplicador_moeda = 5 
bonus_estrela = 2
penalidade = 300

pontuacao_final = (pontos_base + (moedas_coletadas * multiplicador_moeda))**bonus_estrela -penalidade

print(f"A pontuação final do jogador é: {pontuação_final}")