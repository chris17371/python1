#condicional elif else

tipo='estudiante'
if tipo =='estudiante':
    print ('tienes un descuento del 50%')
elif tipo=='profesor':  
    print ('tienes un descuento del 80%')
elif tipo=='invitado':
    print ('tienes un descuento del 10%')
else:
    print ('no tienes descuento') 
    
    
    
    
usuario ='roman'
tipoUsuario = 'admin'
tiposUsuarios = ['admin', 'superadmin', 'usuario']
   
if tipoUsuario in tiposUsuarios and usuario== 'roman':
    if tipoUsuario=='superadmin':
        print ('ACCESO TOTAL')  
    elif tipoUsuario=='admin':
        print ('EL USUARIO ES ADMIN')
    else:
        print ('EL USUARIO ES INVITADO')
else:
    print ('NO HAY ACCESO, NO TIENE ACCESO')
          
        
