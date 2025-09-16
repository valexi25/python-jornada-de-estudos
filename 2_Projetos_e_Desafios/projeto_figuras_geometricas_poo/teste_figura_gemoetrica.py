from cuadrado import Cuadrado
from retangulo import Rectangulo
#from figura_geometrica import FiguraGeometria
#nao se puede instanciar una clase abstracta
#figura = FiguraGeometria()
cuadrado1 = Cuadrado(5,'rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcular_area())

print()
print(' Creación de cuadrado '.center(50,'+'))
print(cuadrado1)
print(' Creación del objeto rectangulo '.center(50,'-'))
rectangulo1 = Rectangulo(3,8,'verde')
print(f'Cálculo área rectángulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

print(' Creación de cuadrado '.center(50,'+'))
cuadrado2 = Cuadrado(5,'azul')
print(cuadrado2)

