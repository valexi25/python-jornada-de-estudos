print("*** calculadora Com validação ***")

numero_1 = float(input('Digite um numero: '))
numero_2 = float(input('Digite otro numero'))
operador = input('Qual operação quer fazer?')

if operador == '+':
    print(f'O resultado de {numero_1} {operador} {numero_2} = {numero_1 + numero_2}')
elif operador == "-":
    print(f'O resultado de {numero_1} {operador} {numero_2} = {numero_1 - numero_2}')
elif operador == "*":
     print(f'O resultado de {numero_1} {operador} {numero_2} = {numero_1 * numero_2}')
elif operador == '/':
    if numero_2 == 0:
        print("Não e posivel dividir por zero.")
    else:
         print(f'O resultado de {numero_1} {operador} {numero_2} = {numero_1 / numero_2}')
else:
    print("Operador não identificado")

