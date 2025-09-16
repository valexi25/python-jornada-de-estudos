from figura_geometrica import FiguraGeometria
from color import Color 
class Rectangulo(FiguraGeometria,Color):
    def __init__(self, ancho, alto,color):
        FiguraGeometria.__init__(self,ancho,alto)
        Color.__init__(self,color)
    
    def calcular_area(self):
        return self.alto * self.ancho
    
    def __str__(self):
        return f'{FiguraGeometria.__str__(self)} {Color.__str__(self)}'
    