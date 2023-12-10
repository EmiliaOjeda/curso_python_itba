import requests
import json
import sqlite3
import matplotlib.pyplot as plt
from get_finanzas import get_finanzas
from crear_tabla_finanzas import crear_tabla_finanzas
from crear_tabla_consultas import crear_tabla_consultas
from escribir_tabla_consultas import escribir_tabla_consultas
from escribir_nuevo_registro import escribir_nuevo_registro
from mostrar_consultas import mostrar_consultas
from crear_grafico import crear_grafico
from get_tickers_disponibles import get_tickers_disponibles

#crear tabla con datos de api
crear_tabla_finanzas()
#crear tabla de tickers consultados
crear_tabla_consultas()

#Solicitar a usuario opción a realizar

print ("Bienvenido. Elija una opción:")
print ("1 - Actualización de datos")
print ("2 - Visualización de Datos")
opcion = input("Su opción es: ")

if (opcion == "1"):

    # ---- HACIENDO REQUEST ---- 

    print ("Ud. eligió opc. 1")

    ticker = input ("Ingrese ticker: ")
    fecha_inicio = input ("Ingrese año de inicio con formato AAAA-MM-DD: ")
    fecha_fin = input ("Ingrese año de fin con formato AAAA-MM-DD: ")
    api_key = "H_DPmhHbXug4HXPLuB5aHj6GG4N0E83k"

    response = get_finanzas (ticker, fecha_inicio, fecha_fin, api_key)

    # ---- GUARDANDO EN BASE DE DATOS ----

    base_de_datos = sqlite3.connect('base_de_datos.db')
    cursor = base_de_datos.cursor()
    escribir_nuevo_registro(ticker, base_de_datos, cursor, response)

    #escribir en base de datos de tickers consultados
    escribir_tabla_consultas(cursor, base_de_datos, ticker, fecha_inicio, fecha_fin)

elif (opcion == "2"):
    print("Visualización de Datos")
    print("Opciones Disponibles: ")
    print("1- Resumen")
    print("2- Gráfico")
    opcion2 = input("Ingrese su respuesta: ")

    if (opcion2 == "1"):
        tickers = get_tickers_disponibles()
        if len(tickers) == 0:
            print("Ticker no disponible en base de datos. Reinicie programa y actualice")
        else:
            print("Mostrando resumen: ")
            mostrar_consultas()
    elif(opcion2 == "2"):
        tickers = get_tickers_disponibles()
        if len(tickers) == 0 :
            print("Ticker no disponible en base de datos. Reinicie programa y actualice")
        else:
            print("Tickers disponibles:")
            for i in tickers:
                print(i[0])
            print(" ")
            ticker_elegido = input ("Elija ticker a graficar: ")
            crear_grafico(ticker_elegido)
            print(" ")
    else:
        print("Opción incorrecta. Terminando el programa")


else:
    print ("Opción incorrecta.")
print (opcion)