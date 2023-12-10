import sqlite3

def get_tickers_disponibles():
    base_de_datos = sqlite3.connect("base_de_datos.db")
    cursor = base_de_datos.cursor()
    cursor.execute("SELECT DISTINCT ticker FROM tabla_finanzas")
    result = cursor.fetchall()
    for i in result:
        print(i)
    return result
