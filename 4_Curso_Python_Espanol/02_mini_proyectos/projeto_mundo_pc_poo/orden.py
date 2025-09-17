
class Orden:
    contador_orden = 0

    def __init__(self,computadoras):
        Orden.contador_orden += 1
        self.id_orden = Orden.contador_orden
        #recibir la lista de objetos de tipo de computadora
        self.computadoras = computadoras
    
    def agregar_computadora(self,computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str += '\n' + computadora.__str__()
        return f'''Ordem {self.id_orden}
        Computadoras: {computadoras_str}'''