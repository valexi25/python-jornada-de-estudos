print("**** Simulador de bateria de celular ***")

#   VOÇÊ VAI SIMULAR O GASTO DA E A RECARGA DA BATERIA DE UM CELULAR AO LONGO DE ALGUMAS ATIVIDADES.
# º1 COMENCE COM A BATERIA CHEIA:
    # 1º CRIE UMA VARIÁVEL nivel_bateria E INICIALIZE-A COM 1OO.
# º2 SIMULE O USO E A RECARGA USANDO OPERADORES DE ATRIBUIÇÃO: 
    # 1º O USUARIO JOGOU UM GAME CONSUMIU 30% DA BATERIA. ATUALIZEI A VARIÁVEL nivel_bateria USANDO O OPERADOR DE ATRIBUIÇÃO (-=).
    # 2º DESPOIS, ELE ASSITIU A UM VÍDEO QUE GASTOU MAIS 20%. ATUALIZE AVARIÁVEL NOVAMENTE.
    # 3º POR FIM, ELE DEU UMA CARGA RÁPIDA QUE RECUPEROU 15%. ATUALIZE AVARIÁVEL USANDO O OPERADOR DE ATRIBUIÇÃO DE ADIÇÃO (+=).
# º3 CALCULE O TEMPO DE VÍDEO RESTANTE:
    # 1º CONSIDERE QUE ASSITIR A UMA HORA DE SÉRIE CONSOME 12% DE BATERIA.
    # 2º CRIE UMA VARIÁVEL horas_video_restantes E CALCULE QUANTAS HORAS INTEIRAS DE SÉRIE O USUÁRIO AINDA CONSEGUE ASSISTIR COM A BATERIA ATUAL. USE O OPERADOR DE DICISÃO INTEIRA (//) PARA ISO.
# º4 VERIFIQUE SE HÁ BATERIA:
    # 1º CRIE UMA VARIÁVEL BOOLEANA  ainda_tem_bateria. ELA DEVE SER TRUE SE O nivel_bateria FOR MAIOR QUE 0, E FALSE CASO CONTRÁRIO.
# º5 IMPRIMA OS RESUKTADOS DE FORMA CLARA:
    # 1º "NIVEL FINAL DA BATERIA: [VALOR]%"
    # 2º "HORAS INTERIRAS DE VIDEO RESTANTES: [VALOR]"
    # 3º "O celular ainda está ligado? [valor]"

nivel_bateria = 100

nivel_bateria -= 30

nivel_bateria -= 20

nivel_bateria += 15

horas_videos_restantes = nivel_bateria // 12

ainda_tem_bateria = nivel_bateria > 0

print(f"Nivel final de bateria:{nivel_bateria}%")
print(f"Horas inteiras de video restantes: {horas_videos_restantes}%")
print(f"O celular ainda está ligado?: {ainda_tem_bateria}")