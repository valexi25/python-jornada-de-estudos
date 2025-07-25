print("*** Positivo,Negativo ou Zero ***")
"""
Objetivo: Agora, vamos usar o elif (uma contração de "else if") para lidar com três condições diferentes.
Você vai criar um programa que verifica se um número é positivo negativo ou zero.
Instruções:
    Crie uma variével chamada numero e atribua um valor numérico a ela (pode ser positivo,negativo ou zero)
    Use uma estrutura if/elif/else:
        if o numero for maior que 0, imprima a mensagem Número Positivo.
        elif o numero for menor que 0, imprima a mensagem Número Negativo.
        else(que cobrirá o caso restante, ou seja quando o número é 0), imprimir O número é zero.
"""
numero =34

if numero >0 :
    print("Número Positivo")
elif numero < 0:
    print("Número Negativo")
else:
    print("O Número é Zero.")