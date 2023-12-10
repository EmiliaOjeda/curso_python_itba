import  sqlite3

def escribir_nuevo_registro(ticker, base_de_datos, cursor, response):
     for dia in response['results']:
        # Escribir en base de datos de finanzas
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
                        precio_medio_ponderado)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (
                        ticker,
                        dia['c'],
                        dia['h'],
                        dia['l'],
                        dia['n'],
                        dia['o'],
                        dia['t'],
                        dia['v'],
                        dia['vw']
                        )
                        )
        base_de_datos.commit()
       