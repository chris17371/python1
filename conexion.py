import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",   
            password="",
            database="clinica",
        )
        print("Conexion con la base de datos, exitosa")
        return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar mysql: {error}")
        return None
    except Exception as error:
        print(f"Error inesperado: {error}")
        return None
    finally:
        if conexion.is_connected():
            print("conexion cerrada")

conectar_bd()