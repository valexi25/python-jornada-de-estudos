print("*** Calculadora de Fretes ***")
"""
Regras:
    SP : R$ 10,00 de taxa fixa
    SUL: R$ 1,50 por peso
    NORDESTE : R$ 2,00 por kg
    NORTE: R$ 2,50
"""
taxa_fixa_15Kg = 20.00
peso_kg = 3
regiao = "SP"
custo_frete = None
if regiao == "SP":
    custo_frete = 10.00
elif regiao == "SUL":
    custo_frete = peso_kg * 1.50
elif regiao == "NORDESTE":
    custo_frete = peso_kg * 2.00
elif regiao == "NORTE":
    custo_frete = peso_kg * 2.50
else:
    custo_frete = 50.00

if peso_kg > 15:
    custo_frete = custo_frete + taxa_fixa_15Kg

print(f"Destino:{regiao}| Peso:{peso_kg}| Custo do Frete: R${custo_frete}")
