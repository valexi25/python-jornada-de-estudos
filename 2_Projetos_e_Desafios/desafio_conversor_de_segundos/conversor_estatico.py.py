print("*** Conversor de Segundos ***")
"""
    IMAGINE QUE VOÇÊ TEM UM VALOR QUE REPRESENTA UMA QUANTIDADE TOTAL DE SEGUNDOS, E SEU OBJETIVO É
    CONVERTER ESSE VALOR PARA O FORMATO DE HORAS,MINUTOS E SEGUNDOS.
    POR EXEMPLO,SE O TOTAL DE SEGUNDOS FOT 3661, O RESULTADO DEVE SER 1 HORA, 1 MINUTO E 1 SEGUNDO.
        SEU DESAFIO
            1º CIRE A VARIÁVEL INICIAL:
                º1 total_de_segundos = 5432
            2º FAÇA OS CÁLCULOS EM ETAPAS:
                1º PRIMEIRO,CALCULE O NÚMERO DE HORAS COMPLETAS.(DICA: UMA HORA TEM 3600 SEGUNDOS).
                2º DEPOIS, CALCULE QUANTOS SEGUNDOS SOBRARAM APÓS EXTRAIR AS HORAS. O OPERADOR MÓDULO(%)
                   É PERFEITO PARA ISSO.
                3º A PARTIR DOS SEGUNDOS QUE SOBRARAM, CALCULE QUANTOS MINUTOS COMPLETOS EXISTEM.(DICA UM MINUTO TEM 60 SEGUNDOS).
                4º FINALMENTE,CALCULE OS SEGUNDOS RESTANTES QUE NÃO FORMARAM UM MINUTO COMPLETO.
            3º  ARMAZEME OS RESULTADOS FINAIS EM TRÊS VARIÁVEIS SEPARADAS:
                1º HORAS
                2º MINUTOS
                3º SEGUNDOS
            4º IMPRIMA O RESULTADO DE FORMA CLARA, POR EXEMPLO:
                1º "O TEMPO CORRESPONDENTE É: [H]HORA,[M]MINUTOS S [S]SEGUNDOS."
            
"""

total_de_segundos = 5432

horas = total_de_segundos // 3600
segundos_restantes_apos_horas = total_de_segundos % 3600
minutos = segundos_restantes_apos_horas // 60
segundos = segundos_restantes_apos_horas % 60

print(f"O tempo corespondente é: {horas} horas,{minutos} minutos,{segundos} segundos")



