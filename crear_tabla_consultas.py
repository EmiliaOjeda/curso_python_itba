import sqlite3

def crear_tabla_consultas():
    base_de_datos = sqlite3.connect("base_de_datos.db")
    cursor = base_de_datos.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS tabla_consultas (
            ticker VARCHAR,
            fecha_inicio VARCHAR,
            fecha_fin VARCHAR
            );
            '''
            )