print("*** Codificador Numérico ***")
"""
Precisa criar um "codificador" que transforma um número de 3 dígitos em outro, seguindo um algoritmo especifico.
    O algoritmo de codificação
        1º separação: dado um número inteiro de 3 digitos(ex:742),você de primeiro separar cada um dos três digitos em variáveis individuais.
            º1 dica: 742// 100 te dá o primeiro digito. Como você pegaria o do meio e o útimo? pense em // e %
            º2 transformação: Aplique uma transformação matemática a cada digito.A regra é: novo_digito = (digito_original + 5) % 10.
                1º isso significa que você soma 5 ao digito e pega o resto da divisão por 10. por exemplo, se o 
                    digito e 7, o novo digito será (7+5)%10 que é 12%10, resultando em 2.
            º3 troca: depois de transformar os três digitos, troque a posição do primeiro com a do terceiro. O digito do meio permanece no lugar.
            º4 Recombinação: junte os digitos transformados e trocados para formar um novo número inteiro de 3 digitos.
                1º dica: Se seus novos digitos são d1,d2,d3, o número final é d1*100 + d2 * 10 + d3.
            Seu desafio:
                1º Crie a variável inicial:
                    1º numero_original = 742
                2º siga os 4 passos do algoritmo(Separação,Transfotmação,Troca,Recombinação)usando
                    variáveis para armazenar os resulrados de cada etapa.
                3º Armazene o resultado final na variável numero_codificado.
                4º imprima o resultado
                    "O número 742 codificado é: [resultado]"         
"""
numero_original = 742
#optenção dos numeros
numero1 = numero_original //100 %100
terninou1 = numero_original %100
numero2 = terninou1 //10 
numero3 = terninou1 % 10
#transformação
novo_digito1 = (numero1+5)%10
novo_digito2 = (numero2+5)%10
novo_digito3 = (numero3+5)%10
#troca
novo_digito1,novo_digito3 = novo_digito3,novo_digito1
#recombinação
novo_numero = (novo_digito1 * 100)+ (novo_digito2 *10) +novo_digito3

print(f"O número 742 codificado é: {novo_numero}")