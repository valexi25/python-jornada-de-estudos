# *args - aguments - tupla
# **kargs -keyword arguments (key,value) como un dict
print('*** Argumentos variables en forma de dict **')

def superheroe_superpoderes(nombre,*args, **kargs):
    print(f'Superheroe: {nombre} - {args} - mas info: {kargs}')

#Lammar la funcion 
superheroe_superpoderes('Spiderman','instinto Aránido', edad= 17,empresa='Marvel')

superheroe_superpoderes('Iroman','Armadura','play boy', edad=45)

#Es opcional enviar argumantos variables
superheroe_superpoderes('Mi vecino')