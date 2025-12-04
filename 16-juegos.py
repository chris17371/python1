#como saber si un numero es par 
numero = input ('agrega un numero y te dire si es impar\r\n')
numero = int(numero)

if numero %2 == 0: #modulo divide para ver si es entero y genera un residuo
    print(f'tu numero {numero} es par')
else:
    print(f'tu numero {numero} es impar')