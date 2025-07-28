print("*** Validador de Notas***")
"""
Objetivo:  Usar o operador lógico (and) dentro de uma condição if para verificar se um valor está dentro de um intervalo.
instruçoes:
    Crie variável chamada nota e atribua um valor numérico a ela.
    Esceva uma estrutura if/else.
    A condição do if deve verificar se a nota é maior ou igual a 0 E, ao mesmo tempo,menor ou igual a 10.
    Se a condição for verdadeira, o programa deve imprimir: Nota invalida.
    Caso contrário (se a nota form menor que 0 ou mair que 10),deve imprimir:Nota invalida

"""
nota = 5
if nota >= 0 and nota <= 10:
    print(f"Nota valida {nota}")
else:
    print("Nota Invalida")