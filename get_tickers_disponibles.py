import sqlite3

'''
Se obtienen tickers disponibles de 'tabla_finanzas'.

'''

def get_tickers_disponibles():

    #conectar a base de datos
    base_de_datos = sqlite3.connect("base_de_datos.db")
    cursor = base_de_datos.cursor()

    #ejecutar consulta SQL para obtener tickers distintos
    cursor.execute("SELECT DISTINCT ticker FROM tabla_finanzas")

    #obtener resultados de consulta
    result = cursor.fetchall()

    #mostrar tickers disponibles
    #for i in result:
    #    print(i)

    #cerrar conexión a base de datos
    base_de_datos.close()

    #devolver lista de tickers disponibles 
    return result
