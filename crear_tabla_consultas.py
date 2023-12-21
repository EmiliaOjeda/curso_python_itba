import sqlite3

'''
Se crea una tabla llamada 'tabla_consultas' en la base de datos 'base_de_datos.db' si no existe.
En ella se almacena información sobre consultas realizadas:
    - nombre ticker
    - fecha inicio
    - fecha fin
    
'''

def crear_tabla_consultas():

    #conectar a la base de datos
    base_de_datos = sqlite3.connect("base_de_datos.db")
    cursor = base_de_datos.cursor()
    
    #definir consulta SQL para crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabla_consultas (
            ticker VARCHAR,
            fecha_inicio VARCHAR,
            fecha_fin VARCHAR
        );
    ''')