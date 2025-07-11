print("**** Casa de los Espejos ***")
"""
Supón que estás en un parque de diversiones y quieres entrar a la casa de los espejos.
Sin embargo debes cumplir con algunas condiciones.
    º1 Debes tener más de 10 años
    º2 No debe darte miedo la oscuridad
Si se cumple las condiciones anteriores puedes entrar.
Para realizar este ejemplo vamos a utilizar el operador not para aplicar una lógica inversa
"""
edad = int(input("Cuál es tu edad? "))
tienes_miedo_oscuridad = input("tienes miedo a la oscuridad (si/no)")
tienes_miedo_oscuridad =tienes_miedo_oscuridad.strip().lower() == 'si'

if not tienes_miedo_oscuridad and edad >= 10:
    print("Puedes entrar a la casa de los espejos")
else:
    print('Lo siento, la casa de los espejos ´pdria darte miedo')