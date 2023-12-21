import  sqlite3

'''
Se escriben nuevos registros en 'tabla_finanzas' con info brindada.

Parámetros:
- ticker (str): símbolo del activo financiero
- base_de_datos: conexión a la base de datos
- cursor: cursor de la base de datos
- response: respuesta de API con clave 'results' con lista de resultados

'''

def escribir_nuevo_registro(ticker, base_de_datos, cursor, response):
    
    for dia in response['results']:
        #escribir en tabla_finanzas
        cursor.execute('''
            INSERT INTO tabla_finanzas (
               ticker, 
               precio_de_cierre,
               precio_max,
               precio_min,
               cantidad_transacciones,
               precio_apertura,
               unix_timestamp,
               trading_volume,
               precio_medio_ponderado
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
         ''', (
            ticker,
            dia['c'],
            dia['h'],
            dia['l'],
            dia['n'],
            dia['o'],
            dia['t'],
            dia['v'],
            dia['vw']
         ))
        
    #guardar cambios
    base_de_datos.commit()
