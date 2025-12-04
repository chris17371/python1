from flask import  Flask, render_template
from conexion import conectar_bd
import mysql.connector

app = Flask(__name__)

def leer_registros():
    """Conecta a la BD lee todos los medico y devuelve una lista de tuplas"""
    conexion = conectar_bd()
    resultados = []
     
    if conexion is None:
        print("Error de conexion a la base de datos")
        return resultados
    
    curso = None
    try:
        curso = conexion.cursor()
        consulta = "SELECT * FROM medico"
        resultados = curso.fetchall()
    
    except mysql.connector.Error as error:
        print(F"Error al leer los datos en el sistema:{error}")
    
    finally:
        if curso is not None:
            curso.close()
        if conexion.is_connected():
            conexion.close()
@app.route('/')
def listar_medico():
    # 1. obtener datos de la base de datos
    datos_medico = leer_registros()
    # 2. renderizar la plantilla HTML pasandole los datos
    return render_template('pasientes.html', medico=datos_medico,titulos="Listado de medico")

# INICIO DEL SERVIDOR 
if __name__ == '__main__':
    app.run(debug=True)