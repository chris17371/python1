playlist = {}

def crear_playlist():
    nombre_playlist = input('Cómo deseas nombrar tu playlist:\n')
    playlist[nombre_playlist] = []
    return nombre_playlist #FUNCION QUE RETORNAN UN VALOR EN ESTE CASO EL NOMBRE DE LA PLAYLIST

def agregar_canciones(playlist_nombre):
    print('Agregando canciones a la playlist', playlist_nombre)
    while True:
        cancion = input('Ingresa el nombre de la canción (o "X" para salir): ')
        if cancion.lower() == 'x':
            break
        playlist[playlist_nombre].append(cancion) #METODO QUE AGREGA UNA CANCION A LA PLAYLIST 
        print('Canción agregada:', cancion)
        
def eliminar_canciones(playlist_nombre):
    print('Eliminando canciones de la playlist: ', playlist_nombre)
    while True:
        cancion_eliminar = input ('Ingresa el nombre de la canción a eliminar (o "X" para salir): ')
        if cancion_eliminar.lower() == 'x':
            break
        if cancion_eliminar in playlist[playlist_nombre]:
            playlist[playlist_nombre].remove(cancion_eliminar)
            print('Canción eliminada:', cancion_eliminar)
        else:
            print('La canción no se encuentra en la playlist.')
            
def mostrar_playlists():
    if not playlist:
        print("No hay playlist creadas.")   
    else:
        for nombre_playlist, canciones in playlist.items():
            print(f"Playlist: {nombre_playlist}")
            for cancion in canciones:
                print(f"- {cancion}")

def app():
    while True:
        print("1. Crear una nueva playlist")
        print("2. Agregar canciones a una playlist")
        print("3. Eliminar canciones a una playlist")
        print("4. Mostrar todas las playlists")
        print("5. salir")
        
        opcion = input("Selecione una opción: ")
        
        if opcion == '1':
            nombre_playlist = crear_playlist()
            agregar_canciones(nombre_playlist)
        elif opcion == '2':
            nombre_playlist = input("A que playlist deseas agregar canciones? ")
            if nombre_playlist in playlist:
                agregar_canciones(nombre_playlist)
            else:
                print("La Playlist no existe.")
        elif opcion == '3':
            nombre_playlist = input("De qué playlist deseas eliminar canciones? ")
            if nombre_playlist in playlist:
                eliminar_canciones(nombre_playlist)
            else:
                print("la playlist no existe.")
        elif opcion == '4':
            mostrar_playlists()
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")
            
app()