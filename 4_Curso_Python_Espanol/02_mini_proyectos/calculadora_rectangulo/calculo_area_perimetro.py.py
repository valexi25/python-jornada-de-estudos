print("Cálculo área y perímetro de un rectángulo ***")
"""
    Se solicita calcular el área y perímetro de um rectángulo aplcando las siguientes fórmulas:
    area = base * altura
    perimetro = 2 * (base + altura)
"""
base = float(input("ingrese a base "))
altura = float(input("ingrese a altura "))

area = base * altura
perimetro = 2 * ( base + altura)
print(f"""
O perimetro es: {perimetro:.2f}\n
A área es: {area:.2f}
""")