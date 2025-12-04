libros_josesito = []
clientes_josesito = []

def agregar_libro():
    while True:
        libro_isbn = input('Ingresa el ISBN del libro (13 dígitos numéricos): ')
        if libro_isbn.isdigit() and len(libro_isbn) == 13:
            if any(libro['isbn'] == libro_isbn for libro in libros_josesito):
                print('Advertencia: Ya existe un libro con este ISBN. Continúa si es una copia diferente.')
            break
        else:
            print('Error: El ISBN debe ser un número de 13 dígitos. Inténtalo de nuevo.')

    libro_autor = input('Ingresa el autor del libro: ')
    libro_titulo = input('Ingresa el título del libro: ')

    while True:
        libro_año = input('Ingresa el año de publicación (4 dígitos): ')
        if libro_año.isdigit() and len(libro_año) == 4:
            break
        else:
            print('Error: El año de publicación debe ser un número de 4 dígitos. Inténtalo de nuevo.')

    while True:
        libro_estado = input('Ingresa el estado del libro (disponible/agotado): ').lower()
        if libro_estado in ['disponible', 'agotado']:
            break
        else:
            print('Error: El estado debe ser "disponible" o "agotado". Inténtalo de nuevo.')

    libros_josesito.append({
        'isbn': libro_isbn,
        'autor': libro_autor,
        'titulo': libro_titulo,
        'año': libro_año,
        'estado': libro_estado
    })
    print(f'Libro "{libro_titulo}" agregado con éxito.')

def agregar_cliente():
    nombre_cliente = input('Ingrese el nombre del cliente: ')
    cedula = input('Ingrese el número de cédula: ')

    while True:
        telefono = input('Ingrese el número de teléfono (11 dígitos): ')
        if telefono.isdigit() and len(telefono) == 11:
            break
        else:
            print('Error: El número de teléfono debe tener 11 dígitos numéricos. Inténtalo de nuevo.')

    carrera = input('Ingresa la carrera que cursas: ')
    direccion_general = input('Ingresa dirección sencilla: ')

    clientes_josesito.append({
        'nombre': nombre_cliente,
        'cedula': cedula,
        'telefono': telefono,
        'carrera': carrera,
        'direccion': direccion_general
    })
    print(f'Cliente "{nombre_cliente}" agregado con éxito.')

def eliminar_libro():
    libro_eliminar = input('Ingresa el título del libro a eliminar (o "X" para salir): ')
    
    if libro_eliminar.lower() == 'x':
        return

    libro_encontrado = False
    for libro in libros_josesito:
        if libro['titulo'].lower() == libro_eliminar.lower():
            libros_josesito.remove(libro)
            print(f'Libro eliminado: {libro_eliminar}')
            libro_encontrado = True
            break
    
    if not libro_encontrado:
        print('Error: El libro no se encuentra en el registro.')

def mostrar_libreria():
    print("\n- Libros Registrados en Librería Josesito -")
    if not libros_josesito:
        print("No hay libros registrados.")
    else:
        for libro in libros_josesito:
            print(f"- Título: {libro['titulo']}, Autor: {libro['autor']}, ISBN: {libro['isbn']}, Año: {libro['año']}, Estado: {libro['estado']}")

def mostrar_clientes():
    print("\n- Clientes Registrados en Librería Josesito -")
    if not clientes_josesito:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes_josesito:
            print(f"- Nombre: {cliente['nombre']}, Cédula: {cliente['cedula']}, Teléfono: {cliente['telefono']}, Carrera: {cliente['carrera']}, Dirección: {cliente['direccion']}")

def llevar_libro():
    libro_titulo = input('Ingresa el título del libro a despachar (o "X" para salir): ')
    if libro_titulo.lower() == 'x':
        return

    nombre_cliente = input('Ingresa el nombre del cliente que se llevará el libro: ')
    
    cliente_encontrado = any(cliente['nombre'].lower() == nombre_cliente.lower() for cliente in clientes_josesito)
    
    if not cliente_encontrado:
        print(f'\nAviso: El cliente "{nombre_cliente}" no está registrado.')
        print('Error: No se puede entregar el libro. Por favor, primero registre al cliente.')
        return 
    
    libro_encontrado = False
    for libro in libros_josesito:
        if libro['titulo'].lower() == libro_titulo.lower():
            libro_encontrado = True
            if libro['estado'] == 'disponible':
                libro['estado'] = 'agotado'
                print(f'\n Éxito: El libro "{libro_titulo}" ha sido entregado a "{nombre_cliente}".')
            else:
                print('\nError: El libro ya está agotado y no se puede entregar.')
            break
    
    if not libro_encontrado:
        print('\n Error: El libro no se encuentra en el registro.')


def devolver_libro():
    libro_titulo = input('Ingresa el título del libro a devolver (o "X" para salir): ')
    
    if libro_titulo.lower() == 'x':
        return
        
    libro_encontrado = False
    for libro in libros_josesito:
        if libro['titulo'].lower() == libro_titulo.lower():
            libro_encontrado = True
            if libro['estado'] == 'agotado':
                libro['estado'] = 'disponible'
                print(f'Exito: El libro "{libro_titulo}" ha sido devuelto.')
            else:
                print('Error: El libro está marcado como "disponible" o su estado es incorrecto.')
            break
    
    if not libro_encontrado:
        print('Error: El libro no se encuentra en el registro.')


def app():
    while True:
        print("\n- MENÚ PRINCIPAL -")
        print("1. Agregar libro al registro")
        print("2. Agregar cliente al registro")
        print("3. Eliminar libro del registro")
        print("4. Mostrar todos los libros registrados")
        print("5. Mostrar todos los clientes registrados")
        print("6. Despacho de libro")
        print("7. Devolución de libros")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_libro()
            
        elif opcion == '2':
            agregar_cliente()
            
        elif opcion == '3':
            eliminar_libro()
        
        elif opcion == '4':
            mostrar_libreria()
                
        elif opcion == '5':
            mostrar_clientes()
            
        elif opcion == '6':
            llevar_libro()
            
        elif opcion == '7':
            devolver_libro()
            
        elif opcion == '8':
            break
        else:
            print("Error: Opción no válida. Por favor, selecciona una opción del 1 al 8.")

app()