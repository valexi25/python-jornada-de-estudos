print("*** Conversor de Notas Escolares ***")

nota_numerica = 50
conseito = ""

if (nota_numerica < 0) or (nota_numerica > 100):
    print("Nota invalida. Por favor, insira um valor entre 0 e 100")
else:
    if nota_numerica >= 90:
        conseito = "A"
    elif (nota_numerica >= 80) and (nota_numerica <= 89):
        conseito = "B"
    elif (nota_numerica >= 70) and (nota_numerica <= 79):
        conseito = "C"
    elif (nota_numerica >=60) and (nota_numerica <= 69):
        conseito = "D"
    else:
        conseito = "F"
    
    print(f" A nota {nota_numerica} corresponde ao conceito {conseito}")