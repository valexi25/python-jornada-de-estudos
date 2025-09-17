print('**** Clase Aritmética ****')

class Arimerica:
    # Python solamente toma el ultimo constructor
    #    def __init__(self, operando1):
    #       self.operando1 = operando1

    def __init__(self, operando1=None ,operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def sumar(self):   
        resultado = self.operando1 + self.operando2
        print(f'A soma de {self.operando1} + {self.operando2} = {resultado:.2f}')
    
    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'El resultado de la resta de {self.operando1} - {self.operando2} = {resultado:.2f}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'El resultado de multiplicar {self.operando1} * {self.operando2}')
    
    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'El resultado de la divicion de {self.operando1} / {self.operando2} = {resultado}')
    

# Programa principal
if __name__ == '__main__':
    print('*** ejemplo  Clase Aritmética ***')
    arimetica1 = Arimerica(5,7)
    print('Primer Objecto')
    arimetica1.sumar()
    arimetica1.restar()
 
    # Segundo objeto
    arimetica2 = Arimerica(12,16)
    print('Segundo Objeto')
    arimetica2.sumar()
    arimetica2.restar()
                     
    #Tercer ojeto
    arimetica3 =Arimerica(1)
    arimetica3.operando2 = 9
    print('Tercer Objecto')
    arimetica3.sumar()

    #Cuarto objeto
    arimetica4 = Arimerica()
    print("Cuarto objeto")
    arimetica4.operando1 =2
    arimetica4.operando2 = 8 
    arimetica4.sumar()

    #Quinto objecto
    print('Quinto objeto')
    arimetica5 = Arimerica(operando2=4,operando1=3)
    arimetica5.sumar()