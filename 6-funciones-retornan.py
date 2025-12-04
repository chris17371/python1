#funciones que retornan valores
def info(nombre):
    return nombre
empleado =info('jenny')
print(empleado)

def sumar(a, b):
    return a + b
resultado = sumar(15, 13)
print(resultado)

def pizza(ingredientes):
    return ingredientes
lista =pizza('peperoni, queso, jamon')
print(lista)


def pizza2(a,b,c):
    return a,b,c
pizza2Cocinada = pizza2 ('salsa','maiz','queso')
print (pizza2Cocinada)