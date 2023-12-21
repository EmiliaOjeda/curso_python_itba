import sqlite3

'''
Se crea una tabla llamada 'tabla_finanzas' en la base de datos 'base_de_datos.db' si no existe.

La tabla contiene columnas para almacenar datos financieros:

c - precio de cierre
h - precio más alto en el período considerado
l - precio más bajo en el período considerado
n - número de transacciones en la "aggregate window"
o - precio de apertura
otc - boolean que indica si es un ticker OTC
t - unix timestamp
v - trading volume
vw - volume weigthed average price

'''

def crear_tabla_finanzas() : 

    #conectar a la base de datos
    base_de_datos = sqlite3.connect('base_de_datos.db')
    cursor = base_de_datos.cursor()

    #definir consulta SQL para crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabla_finanzas (
            ticker VARCHAR, 
            precio_de_cierre NUMBER,
            precio_max NUMBER,
            precio_min NUMBER,
            cantidad_transacciones INT,
            precio_apertura NUMBER,
            unix_timestamp INTEGER,
            trading_volume NUMBER,
            precio_medio_ponderado NUMBER
        );
    ''')
