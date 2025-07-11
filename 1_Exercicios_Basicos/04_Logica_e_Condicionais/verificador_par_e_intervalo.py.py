print("**** Verificador de Número Par e Dentro de um Intervalo ****")

# º1 CRIAR UMA VARIÁVEL CHAMADA NUMERO E ATRIBUIR UM VALOR INTEIRO A ELA (por exemplo,20).
# º2 VERIFICAR DUAS CONDIÇÕES SOBRE ESSA VARIÁVEL: 1º se o número e par (dica:use o operador módulo %). 2º se o número está entre 10 e 30.
# º3 ARMAZENAR O RESULTADO FINAL (TRUE OU FALSE) EM UMA VARIÁVEL CHAMADA condicao_valida. A CONDIÇÃO SÓ E VALIDA SE AMBAS AS VERIFICAÇÕES ACIMA FOREM VERDADEIRAS.
# º4 IMPRIMIR UMA MENSAGEM MOSTRANDO O RESULTADO, POR EXEMPLO:"O número atende aos critérios? [resultado]".

numero = 20

condicao_valida = (numero % 2 == 0 ) and (numero >= 10 and numero <=30)


print(f"O Número atende os criterios? {condicao_valida}")

