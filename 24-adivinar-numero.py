import random

def juego_adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0 
    adivinado = False
    
    print("\n-- Bienvenido al juego de adivinar un numero entre el 1-100 --")
    print("Tienes que adivinar el numero en el menor intento posible")
    
    while not adivinado:
        try:
            intento_usuario = int(input("Ingresa un numero: "))
            intentos += 1
        
            if intento_usuario < 1 or intento_usuario > 100:
               print("Recuerda que el numero debe de estar entre 1 y 100.")
            elif intento_usuario > numero_secreto:
                print("Es muy alto, intenta otra vez :c")
            elif intento_usuario < numero_secreto:
             print("Es muy bajo, intenta de nuevo :c")
            else:
                adivinado = True
                print(f"\nAdivinaste el numero secreto era: ({numero_secreto})")
                print(f"\nLo lograste en el intento NRO({intentos})")
        except ValueError:
            print("Entrada no valida. por favor, ingresa un numero entero")
            
juego_adivinar_numero()