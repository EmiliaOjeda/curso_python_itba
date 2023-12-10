import sqlite3
import json

def mostrar_consultas():
    #mostrar tablas consultadas
    conn = sqlite3.connect("base_de_datos.db")
    cursor = conn.cursor()
    query = "SELECT * FROM tabla_consultas"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        texto = f'{row[0]} -- {row[1]} <--> {row[2]}'
        print(texto)