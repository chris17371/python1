playlist ={}
playlist ['canciones']= []

def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Cómo deseas que se llame la playlist?\n')
        
        if nombre_playlist:
            playlist['nombre']=nombre_playlist
            agregar_playlist=False
            agregar_cancion()
            eliminar_canciones()
            mostrar_resumen()
            
def agregar_cancion():
    print('Agregando canciones a la playlist',playlist ['nombre'])
    while True:
        cancion = input('Ingresa el nombre de la cancion (o "X" para salir): ')
        if cancion.lower()=='x':
            
            break #deja de agregar canciones 
        
        playlist['canciones'].append(cancion)
        
        print('cancion agregada', cancion)
        
    print (['¡Playlist completa!'])
    print (playlist)
    
    
def eliminar_canciones():
    print('Que cancion desdeas eliminar de la playlist? ',playlist['nombre'])
    while True:
        cancion_eliminar = input('Ingresa el nombre de la cancion a eliminar (o "X" para salir)')
        if cancion_eliminar.lower()=='x':
            break
        if cancion_eliminar in playlist['canciones']:
            playlist['canciones'].remove(cancion_eliminar)
            print('Cancion elimindad exitosamente', cancion_eliminar)
        else:
            print ('La cancion no se encuentra en la playlist')
            
    print('¡Playlist actualizada!')
    print(playlist)
    
def mostrar_resumen():
    print(f'Playlist',playlist['nombre'])
    print ('Canciones de la playlist"\r\n')
    for cancion in playlist['canciones']:
        print(cancion)
        
app()