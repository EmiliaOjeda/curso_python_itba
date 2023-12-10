import streamlit as st
import sqlite3
import pandas as pd
from get_finanzas import get_finanzas
from crear_tabla_finanzas import crear_tabla_finanzas
from crear_tabla_consultas import crear_tabla_consultas
from escribir_tabla_consultas import escribir_tabla_consultas
from escribir_nuevo_registro import escribir_nuevo_registro
from mostrar_consultas import mostrar_consultas
import plotly.graph_objects as go
import datetime 

# Solicitar a usuario opción a realizar
st.title("Bienvenido. Elija una opción:")
opcion = st.radio("Opción:", ("Actualización de datos", "Visualización de Datos"))

if opcion == "Actualización de datos":
    st.header("Ud. eligió opción 1")
    ticker = st.text_input("Ingrese ticker:")
    fecha_inicio = st.text_input("Ingrese fecha de inicio (AAAA-MM-DD):")
    fecha_fin = st.text_input("Ingrese fecha de fin (AAAA-MM-DD):")
    api_key = "H_DPmhHbXug4HXPLuB5aHj6GG4N0E83k"  # Reemplaza con tu API key

    if st.button('Actualizar Datos'):
        response = get_finanzas(ticker, fecha_inicio, fecha_fin, api_key)

        crear_tabla_finanzas()

        base_de_datos = sqlite3.connect('base_de_datos.db')
        cursor = base_de_datos.cursor()

        escribir_nuevo_registro(ticker, base_de_datos, cursor, response)

        # Crear base de datos de tickers consultados
        crear_tabla_consultas(cursor)

        # Escribir en base de datos de tickers consultados
        escribir_tabla_consultas(cursor, base_de_datos, ticker, fecha_inicio, fecha_fin)

        st.success('Datos actualizados y guardados en la base de datos.')

elif opcion == "Visualización de Datos":
    st.header("Visualización de Datos")
    st.subheader("Opciones Disponibles:")
    opcion2 = st.radio("Seleccione una opción:", ("Resumen", "Gráfico"))

    if opcion2 == 'Resumen':
        st.subheader('Resumen de Datos')

        # Verificar si la tabla existe
        try:
            base_de_datos = sqlite3.connect('base_de_datos.db')
            df = pd.read_sql_query("SELECT * FROM tabla_finanzas", base_de_datos)
            st.dataframe(df)
        except sqlite3.OperationalError:
            st.warning('La tabla "tabla_finanzas" no existe. Ejecute la opción de actualización de datos primero.')

    elif opcion2 == 'Gráfico':
        st.subheader('Gráfico de Velas')

        # Verificar si la tabla existe
        try:
            base_de_datos = sqlite3.connect('base_de_datos.db')
            df = pd.read_sql_query("SELECT * FROM tabla_finanzas", base_de_datos)

            if not df.empty:
                # Filtrar valores de timestamp no válidos (negativos o fuera de rango)
                df = df[df['unix_timestamp'] > 0]

                if not df.empty:
                    # Convertir el timestamp a formato de fecha legible
                    df['fecha'] = pd.to_datetime(df['unix_timestamp'], unit='s')

                    # Crear el gráfico de velas
                    fig = go.Figure(data=[go.Candlestick(x=df['fecha'],
                                                         open=df['precio_apertura'],
                                                         high=df['precio_max'],
                                                         low=df['precio_min'],
                                                         close=df['precio_de_cierre'])])

                    # Configuración del diseño
                    fig.update_layout(title=f'Gráfico de Velas para {df["ticker"].iloc[0]}',
                                      xaxis_title='Fecha',
                                      yaxis_title='Precio')

                    # Mostrar el gráfico en Streamlit
                    st.plotly_chart(fig)
                else:
                    st.warning('No hay datos válidos para graficar.')
            else:
                st.warning('No hay datos disponibles para graficar.')
        except sqlite3.OperationalError:
            st.warning('La tabla "tabla_finanzas" no existe. Ejecute la opción de actualización de datos primero.')
