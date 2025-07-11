print("*** Verificador de Configuração de servidor ***")
"""
Voçê precisa se um servidor está com una configuração estável e pronto para
entrar em produção (pronta_para_producao).
    As Regras:
        Para o servidor ser considerado pronto, a Condição Essencial deve ser verdadeira E pelo menos
        uma das Opções de Suporte(Redundância ou Desempenho) tambem deve ser verdadeira.
        º1 Condição Essencial(OBRIGATORIA):
            1º O sistema_operacional deve ser "Linux" E a memoria_ram deve ser de 16Gb ou mais.
        º2 E
        º3 Opções de Suporte(pelo menos uma das duas):
            1º Opção de Redundância: O tipo_de_armazenamento é "SSD" E o backup_automatico
                está ativo
            2º ou
            3º Opção de Desempenho: O número de cores_cpu é 8 ou mais E o servico_firewall
                está ativo.
    Seu Desafio:
    1º Crie as variáveis de estado do servidor:
        º1 sistema_operacional = "Linux"
        º2 memoria_ram = 32
        º3 tipo_de_armazenamento = "HDD"
        º4 backup_automatico = true
        º5 cores_cpu = 8
        º6 servico_firewall = true
    2º Crie a Variável boleana pronta_para_producao:
        º1 Traduza toda a lógiva acima em uma única expressão.
        º2 Dica: A estrutura geral será: (Bloco da Condição Essencial) an ((Bloco da Opção de Redundância)or( Bloco de Opção de Desempenho))
            Preste munita atenção nos parênteses aninhados.
    3º Imprima o resultado:
        º1 "Servidor pronto para produção? [resultado]"
"""
#Criar as Variáveis de estado de servidor:
sistema_operacional = "Linux"
memoria_ram = 32
tipo_de_armazenamento ="HDD"
backup_automatico = True
cores_cpu = 8
servidor_firewall = True

condition_essencial = ((sistema_operacional == "Linux") and (memoria_ram >= 16))
redundancia = ((tipo_de_armazenamento == "SSD")and(backup_automatico == True))
desempenho = ((cores_cpu >= 8)and (servidor_firewall == True))
pronta_para_producao = condition_essencial and ((redundancia)or(desempenho))

print(f"Servidor pronto para produção? {pronta_para_producao}")
