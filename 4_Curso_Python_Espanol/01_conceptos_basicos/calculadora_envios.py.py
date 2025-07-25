"""
                    Sistema de Envíos
    Crear un programa para determinar el costo de envíos de un paquete según el destino (nacional o internacional) y el peso del
    paquete.
    costos de tarifas:
        nacional = 10 * kilo
        Internacional = 20 * kilo
    El programa debe solicitar 2 valores:
        Destino (nacional o internacional)
        peso (Kilogramos) del paquete
    Al final debe imprimir el costo de envío del paquete.
"""
print("*** Sistema de Envíos ***")
TARIFA_NACIONAL =10
TARIFA_INTERNACIONAL = 20

destino = input("Ingresa el destino del paquete (nacional/internacional)")
peso = float(input("Ingresa el peso del paquete (en Kg)"))

#Calculo del envio del paquete
costo_envio = None
destino = destino.strip().lower()
if destino == 'nacional':
    costo_envio = peso * TARIFA_NACIONAL
elif destino == 'internacional':
    costo_envio = peso * TARIFA_INTERNACIONAL
else:
    costo_envio = 'destino no conocido'

if costo_envio is not None:
    print(f'El costo del envío del paquete es: ${costo_envio:.2f}')