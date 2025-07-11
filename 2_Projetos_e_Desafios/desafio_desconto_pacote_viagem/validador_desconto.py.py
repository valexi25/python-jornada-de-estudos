print("*** validação de Pacote de Viagem com Desconto ***")
"""
Uma afgêcia de viagens tem uma promoção. Um cliente recebe um desconto especial se as seguintes regras forem atendidas:
    Regras para o desconto: 
        1º O pacote é para 2 o mais pessoas e a duração da viagem é de pelomenos 5 dias ou  cliente é um membro "premiun"
        2º Restinção O desconto Não é valido a viagem for durante um feriado nacional prolongado.
    seu desafio
        1º crie as variáves para uma simulação de reserva:
            º1 numero_de_pessoas = 3
            º2 duracao_dias = 7
            º3 eh_menbro_premium = false
            º4 eh_feriado_prolongado = false
        2º crie a variável booleana recebe_desconto
            º A variável deve ser true apenas se as regras (incluindo a restrição) forem satisfeitas.
            º presente muita atenção em como usar os parênteses () para garantir que a lógica (A e B) ou c seja avaliada antes de aplicar a restrição final com and not.
        3º Imprima o resultado:
            º"Cliente elegível para o desconto? [resultados]"
"""
numero_de_pessoas = 5
duracao_dia = 7
eh_menbro_premium = False
eh_feriado_prolongado = False

criterio_descuntos = (numero_de_pessoas >= 2) and (duracao_dia >= 5) or eh_menbro_premium
recebe_descontos = criterio_descuntos and not eh_feriado_prolongado
print(f"Clientes elegível para o desconto? {recebe_descontos}")
