from dispositivo_entrada import DispositivoEntrada
class Raton(DispositivoEntrada):
    contador_ratone = 0

    def __init__(self,marca,tipo_entrada):
        Raton.contador_ratone +=1
        self.id_raton = Raton.contador_ratone
        #self.marca = marca
        #self.tipo_entrada = tipo_entrada
        super().__init__(marca,tipo_entrada)

    def __str__(self):
        return (f'Id: {self.id_raton}, Marca: {self.marca}, Tipo de entrada: {self.tipo_entrada}')

#Codigo principal
if __name__ == '__main__':
    raton1 = Raton('HP','USB')
    print(raton1)

    raton2 =Raton('ASER',"Bloto")
    print(raton2)