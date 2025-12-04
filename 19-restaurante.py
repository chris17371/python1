restaurante = {}

def crear_menu():
    nombre_menu = input('Cómo deseas nombrar tu menú:\n')
    restaurante[nombre_menu] = []
    return nombre_menu 

def agregar_platos(menu_nombre):
    print('Agregando platos al menú', menu_nombre)
    while True:
        plato = input('Ingresa el nombre del plato (o "X" para salir): ')
        if plato.lower() == 'x':
            break
        restaurante[menu_nombre].append(plato) 
        print('Plato agregado:', plato) 
        
def eliminar_platos(menu_nombre):
    print('Eliminando platos del menú: ', menu_nombre)
    while True:
        plato_eliminar = input ('Ingresa el nombre del plato a eliminar (o "X" para salir): ')
        if plato_eliminar.lower() == 'x':
            break
        if plato_eliminar in restaurante[menu_nombre]:
            restaurante[menu_nombre].remove(plato_eliminar)
            print('Plato eliminado:', plato_eliminar)
        else:
            print('El plato no se encuentra en el menú.')
            
def mostrar_menus():
    if not restaurante:
        print("No hay menús creados.")   
    else:
        for nombre_menu, platos in restaurante.items():
            print(f"Menú: {nombre_menu}")
            for plato in platos:
                print(f"- {plato}")
def app_restaurante():
    while True:
        print("1. Crear un nuevo menú")
        print("2. Agregar platos a un menú")
        print("3. Eliminar platos de un menú")
        print("4. Mostrar todos los menús")
        print("5. salir \r\n")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre_menu = crear_menu()
            agregar_platos(nombre_menu)
            
        elif opcion == '2':
            nombre_menu = input("¿A qué menú deseas agregar platos? ")
            if nombre_menu in restaurante:
                agregar_platos(nombre_menu)
            else:
                print("El menú no existe.")
                
        elif opcion == '3':
            nombre_menu = input("¿De qué menú deseas eliminar platos? ")
            if nombre_menu in restaurante:
                eliminar_platos(nombre_menu)
            else:
                print("El menú no existe.")
                
        elif opcion == '4':
            mostrar_menus()
            
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")
app_restaurante() 

