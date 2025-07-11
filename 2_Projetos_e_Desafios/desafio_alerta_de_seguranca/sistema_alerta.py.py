print("*** Sistema de Alerta de Segurança ***")
"""
Você esta programando um sistema de segurança que dispara um "alerta máximo" se um conjunto complexo de
de condições for atendido.
    Regras para o Alerta Maximo:
        O alerta deve ser true se qualquer uma das tês situações abaxio for verdadeira:
        
        1º Situação A: (O sensor de movimento principal foi ativado) E (o sistema está no modo "Armado") e (a janela da sala foi aberta ou a porta dos fundos foi aberta0.))
        2º Ou
        3º Situação B: (O sensor de pressão do cofre foi ativado E o horário é fora do expediente).
        4º ou
        5º Situação C: O botão de pânico foi pressionado.
    seu desafio:
        º1 criar as variáveis de estado do sistema:
            sensor_movimento_ativo = true
            sistema_armado = true
            janela_aberta = false
            sensor_cofre_ativo = false
            fora_de_horario = true
            botao_panico_pressionado = false
        º2 crie uma única variável booleana alerta_maxima:
            º1 traduza as três situações (A,B e c) em uma expressão lógica.
            º2 Dica cruacial: A "Situação A" é a mais complexa. ela mesma é composta por duas partes
                que precisam ser agrupadas com parênteses, antes de serem unidas ás outras
                situações com or. A esterutura geral será (Bloco Lógico da situação A) or (bloco lógico da
                situação B) or (bloco lògico da Situação C).
        º3 imprima o resultado
            º1"Dispara alerta máximo? [resultado]"
"""
# criar as variaves
sensor_movimento_ativo = True
sistema_armado = True
janela_aberta = False
porta_aberta = True
sensor_cofre_ativo = False
fora_de_horario = True
botao_panico_pressionado = False
#criar as situações
situacao_A = ((sensor_movimento_ativo == True) and (sistema_armado == True)) and ((janela_aberta == True)or(porta_aberta == True))

situacao_B = ((sensor_cofre_ativo == True)and(fora_de_horario == True))

situacao_C = (botao_panico_pressionado == True)

alerta_maximo = (situacao_A or situacao_B or situacao_C)

print(f"Disparar alerta Máxomo? {alerta_maximo}")

