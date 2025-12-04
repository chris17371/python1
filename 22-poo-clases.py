class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        
    def encender(self):
        self.encendido = True
        print("El carro ha encendido.")
        
    def apagar(self):
        self.encendido = False
        print("El carro esta apagado.")
        
    def acelerar(self):
        if self.encendido:
            print("El carro esta acelerando.")  
        else:
            print("El carro debe de estar encendido par aacelerar.")
            
            
def acelerar(self):
    if self.encendido:
        print ("El carro esta acelerando.")
        
        
mi_carro = Carro ("toyota","corolla","Rojo")

print(mi_carro.marca)

mi_carro.encender()
mi_carro.acelerar()
        
        
class Calculadora:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def suma(self):
        suma = self.num1+self.num2
        print(f"La suma es: {suma}")
        
    def resta(self):
        resta = self.num1-self.num2
        print(f"La resta es: {resta}")
        
    def multi(self):
        multi = self.num1*self.num2
        print(f"La multiplicacion es: {multi}")
        
    def division(self):
        division = self.num1/self.num2
        print(f"La division es: {division}")
        
mi_suma = Calculadora (10,20)
mi_resta = Calculadora (10,20)
mi_multi = Calculadora (10,20)
mi_division = Calculadora (10,20)
mi_suma.suma()
mi_resta.resta()
mi_multi.multi()
mi_division.division()        
