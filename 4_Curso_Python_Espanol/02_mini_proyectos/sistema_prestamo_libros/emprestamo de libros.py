print("**** Emprestimo de Libros ****")
# SE PIDE CREAR UN SISTEMA PARA UMA BIBLIOTECA, LA CUAL DESEA PRESTAR LIBROS SI CUMPLE CON CUALQUIERA DE LAS SIGUINTES CONDICIONES.

#   º1 EL USUARIO TIENE CREDENCIAL DE ESTUDANTE
#   º2 EL USUARIO VIVE A NO MÁS DE 3 KM A LA REDONDA 

# SI CUMPLE CON CUALQUIERA DE ESTAS CONDICIONES SE LE PUEDE PRESTAR EL LIBRO.

print('*** Sistema Prestamo de libros ***')

DISTANCIAS_PERMITIDA_KM = 3
tienes_credencial = input("Cuentas con una credencial de estudante (si/no)")
distancia_bivlioteca_km = int(input('A cuantos Km vives de la biblioteca? '))

es_elegible_prestamo = (tienes_credencial.strip().lower() == 'si' or distancia_bivlioteca_km <= DISTANCIAS_PERMITIDA_KM)

print(f"Eres elegible para prestamo de libros? {es_elegible_prestamo} ")