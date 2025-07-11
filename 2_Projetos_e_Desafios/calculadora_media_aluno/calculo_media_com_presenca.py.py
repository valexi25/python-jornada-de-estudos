print("*** Desafio Aprovação com Condição adicional***")

#imagine que, na mesma escola do desafio anterior, o aluno não precisa apenas de uma médida boa para ser aprovado, ele também precisa ter uma frequência minima de aulas.
# º1 MÉDIA FINAL MAIOR OU IGUAL A 7.0.
# º2 PRESENÇA EM PELO MENOS 80% DAS AULAS.

#   INSTRUÇÕES:
#  º1 REUTILIZE AS VARIÁVEIS nota1,nota2,nota3 e media DO exercício anterior. PODE USAR OS MESMOS VALORES OU OUTROS, SE PREFERIR.
#  º2 CRIE UMA NOVA VARIÁVEL CHAMADA percentual_presenca E ATRIBUA A ELA UM VALOR, POR EXEMPLO, 0.85(QUE REPRESENTA 85% DE PRESENÇA).
#  º3 CRIE A VARÍAVEL media_aprovacao COM VALOR 7.0.
#  º4 CRIE A VARIÁVEL presenca_minima COM VALOR 0.80.
#  º5 AGORA, O PASSO PRINCIPAL: CRIE UMA VARIÁVEL FINAL.ELA DEVE USAR O OPERADOR LÓGICO AND PARA VERIFICAR SE A media DO ALUNO É MAIOR OU IGUAL À media_aprovado E SE O percentual_presenca é maior ou igual À presenca_minima.
#  º6 IMPRIMA O RESULTADO FINAL.

nota1 = 10
nota2 = 10
nota3 = 10
percentual_presenca = 0.85
presenca_menima = 0.80
media = (nota1+nota2+nota3)/3

aprocado = (media >= 7.0) and (percentual_presenca >= presenca_menima)

print(f"Sua media é: {media}")
print(f"o persentual de precenca é: {percentual_presenca}")
print(f"voce foi aprovado: {aprocado}")

