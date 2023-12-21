import sqlite3

'''
Se muestran consultas almacenadas en 'tabla_consultas' de 'base_de_datos.db'.

'''

def mostrar_consultas():
    
    #conectar a base de datos
    conn = sqlite3.connect("base_de_datos.db")
    cursor = conn.cursor()

    #seleccionar todo de tabla_consultas
    query = "SELECT * FROM tabla_consultas"
    cursor.execute(query)

    #obtener resultados de consulta
    results = cursor.fetchall()

    #mostrar resultados
    for row in results:
        texto = f'{row[0]} -- {row[1]} <--> {row[2]}'
        print(texto)

    #cerrar conexión a base de datos
    conn.close()