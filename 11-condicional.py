#operadores de comparacion
# == igual a 
# < menor que
# > mayor que
# <= menor o igual que 
# >= mayor o igual que 

a = 5
b = 3
igual = a == b # igual es false
diferente = a != b #difrente true
mayor = a >= b # mayor es true

#CONDICIONAL
ahorro = 0
if ahorro >=50:
    print("Nos vamos de viaje")
else:
    print("no hay billete")
    
    
lenguaje = 'python'
if not lenguaje =='python':
    print (f'super eres un pro en {lenguaje}')
else:
    print(f'no eres un pro en {lenguaje}')
    
    

usuario_autenticado = False
if usuario_autenticado :
    print('el usuario se autentico con exito')
else:
    print('el usuario no se autentico vuelva a intentarlo')
    
    
    
supervillanos = ['joker','el pinguino','harley quinn','misterio','cara de barro']
if 'harley quinn' in supervillanos:
    print('adoras a harley quinn')
else:
    print('tu no adoras a harley >:c')
    
    
tipousuarios = ['superadmin','admin','invitado']
if 'admin' in tipousuarios:
    print('tienes acceso')
else:
    print('no tienes acceso')
    

#condicionales anidados

acceso_usuario = True
acceso_admin = False

if acceso_usuario:
    if acceso_admin:
        print('ACCESO TOTAL')
    else:
        print ('el usuario no es admin')
else:
    print('el usuario no esta autenticado')