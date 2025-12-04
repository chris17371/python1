nombre = input('cual es tu nombre?\r\n')
print (f'tu nombre es {nombre}')


edad = input ('cual es tu edad?\r\n')
#convertir edad en un entero (int) float(decimal) (srt)
edad = int (edad)

if edad>=18:
    print(f'eres mayor de edad y puedes votar')
else:
    print(f'lo sentimos aun un un nene JASDJASDH')
    
    
#caso en el que un usuario ingrese otro valor que no se un numero
edad=input('¿cual es tu edad?')
try:
    edad=int (edad)
    if edad >= 18:
        print(f'Eres mayor de edad y pruedes votar')
    else:
        print (f'Aún no tienes la edad para votar')
except ValueError:
    print("por favor, ingrese un numero valido para la edad")

