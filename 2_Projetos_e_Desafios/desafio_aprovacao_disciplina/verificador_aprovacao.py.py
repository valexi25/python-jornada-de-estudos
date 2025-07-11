print("*** Aprovação em Diciplina Escolar ***")
"""
Agora,vamos para um exercício focado em usar os parênteses() para dizer ao python qual lógica agrupar primeiro.
um aluno é aprovado em uma diciplina se uma das duas situações abaixo acontecer:
    1º A nota do exame final maior ou igual a 6 E a nota do projeto final for maior ou igual a 6
    2º ou
    3º A média de todos os trabalhos for maior ou igual a 8 E a frequência do aluno for maior ou igual a 90%.
    
    seu Desafio:
        °1 nota_exame_final = 7.0
        º2 nota_projeto = 5.0
        º3 media_trabalho = 8.5
        º4 frequencia = 95
    2º Crie a variável booleana aluni_aprovado
        º1 você vai precisar agrupar a Situação 1 com parênteses()
        º2 você vai precisar agrupar a Situação 2 com parênteses()
        º3 Depois, você vai conetar esses dois grupos com o operador or.
    3º Imprima o resultado:
        "O aluno foi aprovado? [resultado]
"""
nota_exame_final = 7.0
nota_projeto = 5
media_trabalho = 8
frequencia = 95
situacao_1 =(nota_exame_final >= 6 and nota_projeto >= 6)
situacao_2 = (media_trabalho >= 8 and frequencia >= 90)

aluno_aprovado =(situacao_1 or situacao_2)
print(f"O aluno foi aprovado? {aluno_aprovado}")