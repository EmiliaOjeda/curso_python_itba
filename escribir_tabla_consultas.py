def escribir_tabla_consultas(cursor, base_de_datos, ticker, fecha_inicio, fecha_fin):
    cursor.execute('''
                        INSERT INTO tabla_consultas (
                        ticker,
                        fecha_inicio,
                        fecha_fin)
                        VALUES (?, ?, ?)''',
                        (
                        ticker,
                        fecha_inicio,
                        fecha_fin
                        )
                        )

    base_de_datos.commit()
