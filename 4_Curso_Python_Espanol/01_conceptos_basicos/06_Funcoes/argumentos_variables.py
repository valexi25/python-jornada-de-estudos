print('*** Argumentos Variables ****')

def superheroe_superpoderes(superheroe,nombre,*args):
    print(f"Superheroe: {superheroe} - {nombre} - {args}")
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

# Llamar la funcion

superheroe_superpoderes('Spiderman', 'Piter Parqueer', 'instinto arácnido','Telaarña' )
superheroe_superpoderes('Iromam','Tony star', 'armadura','playboy','millonario')

# Es opcional enviar arqumentos variables
superheroe_superpoderes('Mi vecino','Juan')