import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime

def crear_grafico(ticker):

    base_de_datos = sqlite3.connect("base_de_datos.db")
    cursor = base_de_datos.cursor()

    cursor.execute(
        '''
        SELECT DISTINCT unix_timestamp, precio_apertura FROM tabla_finanzas
        WHERE ticker = ?
        ''',
        (ticker,)
    )

    query_result = cursor.fetchall()

    print(query_result)

    timestamps = []
    precios = []

    for i in query_result :
        print(i)
        timestamps.append(i[0])
        precios.append(i[1])

    print(timestamps)
    print(precios)

    dates = []
    for i in timestamps:
        dates.append(datetime.utcfromtimestamp(i/1000).strftime("%Y-%m-%d"))

    date_objects = [datetime.strptime(date, "%Y-%m-%d").date() for date in dates]

    plt.plot(date_objects, precios, marker="o")
    plt.xlabel("Fecha")
    plt.ylabel("Precio")
    plt.title("Evolución de precio")
    plt.show()