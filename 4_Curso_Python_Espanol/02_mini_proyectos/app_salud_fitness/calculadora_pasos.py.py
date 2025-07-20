""" 
Se solicita crear una aplicación de salud y fitness que solicite lo siguiente: 
    Nobre del usuario
    Pasos caminados en el dia
Ademar definiremos las siguientes constantes:
        META_PASOS_DIARIOS = 10000
        CALORIAS_POR_PASO = 0,04 
Con los valores anteriores debemos calcular las calorias quemadas según los pasos caminados
calorias_quemadas según los pasos caminados

    calorias_quemadas = pasos_diarios  * CALORIAS_POR_PASO
Y verificaremos si se cumplió la meta de pasos diarios 
    meta_alcanzada = pasos_diadios >= Meta_PASOS_DIARIOS
"""
print(f"*** Aplicación de salud y Fitness ***")
#Contantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04

#pedimos valores al usuario
nombre_usuario = input('Cual es tu nombre? ')
pasos_diarios = int(input('Cuántos pasos has caminado hoy? '))

#verificar si el usuario alcanzo la meta de passos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'si' if meta_alcanzada else 'No'
#calculamos las calorias quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostrar la informacion
print(f'\nUsuario: {nombre_usuario}\nPasos dados hoy: {pasos_diarios}\nCalorias quemadas: {calorias_quemadas} Kcal \nMeta de passos diarios alcazada: {meta_alcanzada_txt}')
print(f"La meta de Pasos diarios es de : {META_PASOS_DIARIOS} ")