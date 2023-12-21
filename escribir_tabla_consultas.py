'''
Se inserta nueva fila en 'tabla_consultas' con info de consulta realizada.

Parámetros:
- cursor: cursor de la base de datos
- base_de_datos: conexión a la base de datos
- ticker (str): símbolo del activo financiero
- fecha_inicio (str): fecha de inicio en formato 'AAAA-MM-DD'
- fecha_fin (str): fecha de fin en formato 'AAAA-MM-DD'

'''

def escribir_tabla_consultas(cursor, base_de_datos, ticker, fecha_inicio, fecha_fin):
    
    #definir consula SQL para insertar en tabla_consultas
    cursor.execute('''
        INSERT INTO tabla_consultas (
            ticker,
            fecha_inicio,
            fecha_fin
        )
        VALUES (?, ?, ?)
    ''', (ticker, fecha_inicio, fecha_fin))

    #guardar cambios en base de datos
    base_de_datos.commit()
