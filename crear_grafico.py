import sqlite3
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import locale

'''
Se crean 2 gráficos:
- gráfico de velas: muestra evolución diaria de precio de apertura y de cierra, con valores máximos y mínimos del día
- gráfico de barras: muestra evolución diaria de volumen (trading_volume: cant. acciones negociadas en día específico)

En ambos el eje x representa la fecha.
Se grafica para el ticker consultado.

'''

def crear_grafico(ticker):

    #conectar a base de datos
    base_de_datos = sqlite3.connect("base_de_datos.db")
    cursor = base_de_datos.cursor()

    #ejecutar consulta SQL para obtener datos de interés
    cursor.execute(
        '''
        SELECT unix_timestamp, precio_apertura, precio_max, precio_min, precio_de_cierre, trading_volume
        FROM tabla_finanzas
        WHERE ticker = ?
        ''',
        (ticker,)
    )

    #obtener resultados de consulta
    query_result = cursor.fetchall()

    #verificar si hay datos para ticker especificado
    if not query_result:
        print("No hay datos para el ticker especificado.")
        return

    #procesar resultados de la consulta
    timestamps = []
    ohlc_data = []
    volumen_data = []

    for i in query_result:
        timestamps.append(i[0])
        ohlc_data.append((i[0], i[1], i[2], i[3], i[4]))
        volumen_data.append(i[5])

    #convertir tiempos a fechas
    dates = [datetime.utcfromtimestamp(i / 1000).strftime("%Y-%m-%d") for i in timestamps]

    #crear DataFrame de pandas con datos procesados
    df = pd.DataFrame(ohlc_data, columns=['timestamp', 'open', 'high', 'low', 'close'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)

    #crear figura con cuadrícula de 2 filas y 1 columna
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1]})

    #dibujar velas en el primer conjunto de ejes (arriba)
    candlestick_ohlc(ax1, zip(mdates.date2num(df.index), df['open'], df['high'], df['low'], df['close']), width=0.6, colorup='g', colordown='r')

    #agregar etiquetas de precio apertura (o) y cierre (c)
    for i in range(len(df)):
        #ax1.text(df.index[i], df['open'][i], f"o = {df['open'][i]:.2f}", ha='right', va='bottom', color='black', fontsize=8)
        ax1.text(df.index[i], df['close'][i], f"c = {df['close'][i]:.2f}", ha='right', va='top', color='black', fontsize=8)

    #configurar ejes y título
    ax1.set_ylabel("Precio")
    ax1.set_title(f'Evolución de precio y volumen - {ticker}')
    ax1.xaxis_date()  # Configurar el eje x para mostrar las fechas

    #dibujar barras de volumen en el segundo conjunto de ejes (abajo)
    bars = ax2.bar(df.index, volumen_data, color='blue', alpha=0.5, width=0.6, align='center')

    #configurar ejes
    ax2.set_xlabel("Fecha")
    ax2.set_ylabel("Volumen")

    #convertir valores de volumen a cadenas con separadores de miles
    formatted_volumen_data = [locale.format_string("%d", val, grouping=True) for val in volumen_data]

    #agregar etiquetas de valor 
    ax2.bar_label(bars, labels=formatted_volumen_data, label_type='edge', fontsize=8, color='black')

    #ajustar diseño para evitar superposiciones
    plt.tight_layout()

    #mostrar la ventana con ambos gráficos
    plt.show()

    #cerrar la conexión a la base de datos
    base_de_datos.close()

#configurar localización para usar separadores de miles
locale.setlocale(locale.LC_ALL, '')




