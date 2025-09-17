from teclado import Teclado
from monitor import Monitor
from raton import Raton
from computadora import Computadora
from orden import Orden
print('*** Mundo Pc ***')

#Computadora 1 
teclado1 = Teclado('PH','Bluetooth')
raton1 = Raton('Hp','Usb')
monitor1 = Monitor('Dell',15)
computadora1 = Computadora('HP',monitor1,teclado1,raton1)

teclado2 = Teclado('HP','Usb')
raton2 = Raton('Hp','UBS')
monitor2 = Monitor('Gamer',45)
computadora2 = Computadora('Gamer',monitor2,teclado2,raton2)

#Crear la lista de computadoras
computadoras1 = [ computadora1,computadora2]
orden1 = Orden(computadoras1)


teclado3 = Teclado('Dell','Bluetooth')
raton3 = Raton('Dell','Bluetooth')
monitor3 = Monitor('Dell',27)
computadora3 = Computadora('Dell',monitor3,teclado3,raton3)
orden1.agregar_computadora(computadora3)
print()
print(orden1)