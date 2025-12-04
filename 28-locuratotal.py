from conexion import conectar_bd
import mysql.connector

def agregar_cita(conexion):

    try:
        id_paciente = int(input("Ingrese ID del Paciente: "))
        id_especialidad = int(input("Ingrese ID del especialidad: "))
        id_medico = int(input("Ingrese ID del medico: "))
        fecha = input("Ingrese Fecha (YYYY-MM-DD): ")
        hora = input("Ingrese Hora (HH:MM): ")
    except ValueError:
        print("\nEntrada no válida. Asegúrese de ingresar números para los IDs.")
        return

    consulta = "INSERT INTO citas (id_paciente, id_especialidad, id_medico, fecha, hora) VALUES (%s, %s, %s, %s, %s)"
    valores = (id_paciente, id_especialidad, id_medico, fecha, hora)
    cursor = conexion.cursor()
    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        print("\nCita agregada exitosamente.")
        
    except mysql.connector.IntegrityError as error:
        print(f"\nError de integridad al insertar: {error}")
        print("Verifique que los IDs de Paciente, Médico y Servicio sean válidos.")
    except mysql.connector.Error as error:
        print(f"\nError general de MySQL: {error}")      
    finally:
        cursor.close()
        
        
def leer_registros(conexion):
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT c.*, p.*, m.* FROM `citas` c INNER JOIN paciente p ON c.ID_pacientes = p.ID INNER JOIN medico m ON c.ID_medico = m.ID WHERE c.ID_pacientes = 1;")
        resultados = cursor.fetchall()
        for citas in resultados:
            print(citas)        
    except mysql.connector.Error as error:
        print(f"Error al leer los registros: {error}")
    finally:
        cursor.close()
        
conexion = conectar_bd()
        
def app():
    
    try:
        while True:
            print("1. Mostrar citas")
            print("2. Agregar cita")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                leer_registros(conexion)
            elif opcion == '2':
                agregar_cita(conexion)
            elif opcion == '3':
                break
    finally:
        if conexion and conexion.is_connected():
            conexion.close()
            print("Conexión a la base de datos cerrada.")
app()