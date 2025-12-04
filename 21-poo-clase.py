class Restaurante:
    def agregar_restaurante(self,nombre):
        self.nombre = nombre
        print (f'Agregar restaurante: {self.nombre}')
    def mostrar_informacion(self):
        print(f"Elnombre del restaurante es: {self.nombre}")
        
        
#instanciar la clase
restaurante = Restaurante()
restaurante.agregar_restaurante("El pollo loco")
restaurante.mostrar_informacion()

#se pueden crear diferentes objetos con la misma clase     
        
        
class Carro:
    def agregar_carro(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        print(f"Agregar carro: {self.marca,self.modelo,self.color}")
        
        
carro = Carro()
carro.agregar_carro("corsita","corsita","tunning")
print(f"El modelo del carro es {carro.modelo}")      
carro2 = Carro()
carro2.agregar_carro("ford","fortuna","negro")
print(f"la marca de mi carro es: {carro2.marca} el modelo es: {carro2.modelo} y el color es: {carro2.color}")  
        