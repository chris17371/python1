from conexion import conectar_bd
import mysql.connector

def agregar_registro(conexion):
    print("\n--- Ingresar Nuevo Cliente1 ---")
    Nombre = input("Nombre: ")
    Apellido = input("Apellido: ")
    Direccion = input("Direccion: ")
    Telefono = input("Telefono: ")
    Cedula = input("Cedula: ")
    FechaDenacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    Correo = input("Correo: ")

    cursor = conexion.cursor()
    sql = "INSERT INTO clientes (Nombre, Apellido, Direccion, Telefono, Cedula, FechaDenacimiento, Correo) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores = (Nombre, Apellido, Direccion, Telefono, Cedula, FechaDenacimiento, Correo)
    
    try:
        cursor.execute(sql, valores)
        conexion.commit()
        print("Tus datos se han ingresado con exito.")
    except mysql.connector.Error as error:
        print(f"Error al ingresar el registro: {error}")
    finally:
        cursor.close()

def leer_registros(conexion):
    print("\n--- Lista de clientess ---")
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        
        if not resultados:
            print("No hay registros guardados.")
        else:
            for clientes in resultados:
                print(clientes)
    except mysql.connector.Error as error:
        print(f">> Error al leer los registros: {error}")
    finally:
        cursor.close()

def actualizar_registro(conexion):
    print("\n--- Actualizar Telefono ---")
    id_clientes = None
    
    while True:
        try:
            val = input("ID a actualizar (Enter para cancelar): ")
            if not val: return
            id_clientes = int(val)
            break
        except ValueError:
            print("ID invalido. Debe ser un numero entero.")

    nuevo_telefono = input("Nuevo telefono: ")

    cursor = conexion.cursor()
    try:
        sql = "UPDATE clientes SET Telefono = %s WHERE ID = %s"
        valores = (nuevo_telefono, id_clientes)
        cursor.execute(sql, valores)
        conexion.commit()
        
        if cursor.rowcount:
            print("Tus datos se actualizaron con exito.")
        else:
            print("No se encontró ningun registro con ese ID.")
    except mysql.connector.Error as error:
        print(f"Error al actualizar el registro: {error}")
    finally:
        cursor.close()

def eliminar_registro(conexion):
    print("\n--- Eliminar clientes ---")
    id_clientes = None

    while True:
        try:
            val = input("ID a eliminar (Enter para cancelar): ")
            if not val: return
            id_clientes = int(val)
            break
        except ValueError:
            print("ID invalido. Debe ser un numero entero.")

    cursor = conexion.cursor()
    try:
        sql = "DELETE FROM clientes WHERE ID = %s"
        valores = (id_clientes,) 
        cursor.execute(sql, valores)
        conexion.commit()
        
        if cursor.rowcount:
            print("Tus datos se eliminaron con exito.")
        else:
            print("No se encontro ningun registro con ese ID.")
    except mysql.connector.Error as error:
        print(f"Error al eliminar el registro: {error}")
    finally:
        cursor.close()

def app():
    conexion = conectar_bd()
    
    if not conexion:
        print("No se pudo conectar a la base de datos.")
        return

    try:
        while True:
            print("\n- MENU PRINCIPAL -")
            print("1. Agregar clientes al registro")
            print("2. Eliminar clientes del registro")
            print("3. Mostrar clientess del registro")
            print("4. Actualizar teléfono del clientes")
            print("5. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == '1':
                agregar_registro(conexion)
                
            elif opcion == '2':
                eliminar_registro(conexion)
                
            elif opcion == '3':
                leer_registros(conexion)
                
            elif opcion == '4':
                actualizar_registro(conexion)
                
            elif opcion == '5':
                
                break
            else:
                print("Error: Opción no valida.")
    finally:
        if conexion.is_connected():
            conexion.close()
            print("Conexión cerrada.")

app()
