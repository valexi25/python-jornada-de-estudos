print("*** Sitemas PREsTAMO DE LIVROS *****")
"""
Se pide crear un sistema para una biblioteca, la cual desea prestar liobors
si cumple con cualquiera de las siguintes condiciones.

    º1 El usuario tine credencial de estudante
    º2 El usuario vive a no más de 3km a la redonda
si cumple con cualquiera de estas condiciones se le pode prestar um libvro
"""
DISTANCIA_PERMITIDA = 3
tiene_credenciales = input('Cuentas con credencial de estudiante: (emenplo sim/nao)')
distanciacia_biblioteca_km = int(input('A que distancia vives de la biblioteca?: '))

validacao = (tiene_credenciales.strip().lower() == "sim") or (distanciacia_biblioteca_km <= distanciacia_biblioteca_km)
print(f"Eres elegible para prestamos? {validacao}")

