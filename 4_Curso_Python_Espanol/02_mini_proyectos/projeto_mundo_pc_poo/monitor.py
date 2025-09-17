class Monitor:
    contador_monitores = 0
    
    def __init__(self,marca,tamano):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamano = tamano

    def __str__(self):
        return f'Id: {self.id_monitor}, Marca: {self.marca},Tamaño: {self.tamano}'
    
if __name__ == '__main__':
    monito1 = Monitor('HP',15)
    print(monito1)

    monito2 = Monitor('Dell',27)
    print(monito2)