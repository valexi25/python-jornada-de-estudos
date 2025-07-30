print("*** Calculadora de IMC ***")

peso_kl = float(input('Ingrese seu pesso em kg '))
altura_metros = float(input('Ingrese sua altura em Mtrs'))

if not(peso_kl > 0 and altura_metros >0):
    print('Peso e altura devem ser valores positivos')
else:
    imc = peso_kl /(altura_metros * altura_metros)
    print(f"Sue IMC é {imc:.2f}")

    if imc < 18.5: 
        print("Abaixo do peso")
    elif 18.5 <= imc < 25 :
        print('Peso Normal')
    elif 25 <= imc < 30:
        print('Sobrepeso')
    elif 30 <= imc < 35:
        print('Obesidade Grau I')
    elif 35 <= imc < 40:
        print("Obesidade Drau I")
    else:
        print("Obesidade Grau III (Mórbida)")