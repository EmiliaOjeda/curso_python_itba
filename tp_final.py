import sys
import sqlite3
from get_finanzas import get_finanzas
from crear_tabla_finanzas import crear_tabla_finanzas
from crear_tabla_consultas import crear_tabla_consultas
from escribir_tabla_consultas import escribir_tabla_consultas
from escribir_nuevo_registro import escribir_nuevo_registro
from mostrar_consultas import mostrar_consultas
from crear_grafico import crear_grafico
from get_tickers_disponibles import get_tickers_disponibles

#se define la key de la API como constante global
API_KEY = "H_DPmhHbXug4HXPLuB5aHj6GG4N0E83k"

def main():
    while True:
        #imprimir menú principal
        print_menu()
        opcion = input("Su opción es: ")

        if opcion == "1":
            #lógica para actualizar datos
            actualizar_datos()
        elif opcion == "2":
            #lógica para visualizar datos
            visualizar_datos()
        else:
            print("Opción incorrecta.")

        print("¿Desea realizar otra operación?")
        salir = input("Ingrese 's' para salir, cualquier otra tecla para continuar: ")

        if salir.lower() == 's':
            print("Saliendo del programa. ¡Hasta luego!")
            sys.exit()

def print_menu():
    #imprimir menú principal
    print("¡Bienvenido! Elija una opción:")
    print("1 - Actualización de datos")
    print("2 - Visualización de Datos")

def actualizar_datos():
    #crear tablas si no existen
    crear_tabla_finanzas()
    crear_tabla_consultas()

    ticker = input("Ingrese ticker: ")
    fecha_inicio = input("Ingrese fecha de inicio con formato AAAA-MM-DD: ")
    fecha_fin = input("Ingrese fecha de fin con formato AAAA-MM-DD: ")

    #realizar solicitud a API para obtener datos
    response = get_finanzas(ticker, fecha_inicio, fecha_fin, API_KEY)

    #conectar a base de datos
    base_de_datos = sqlite3.connect('base_de_datos.db')
    cursor = base_de_datos.cursor()

    #bloque try-except para manejo de errores que puedan ocurrir durante ejecución de programa
    try:
        #escribir nuevo registro en tabla finanzas
        escribir_nuevo_registro(ticker, base_de_datos, cursor, response)
        #escribir en tabla consultas
        escribir_tabla_consultas(cursor, base_de_datos, ticker, fecha_inicio, fecha_fin)
    except Exception as e:
        print(f"Error al actualizar datos: {e}")

    #cerrar conexión a base de datos
    base_de_datos.close()

def visualizar_datos():
    print("Visualización de Datos")
    print("Opciones Disponibles: ")
    print("1- Resumen")
    print("2- Gráfico")
    opcion2 = input("Ingrese su respuesta: ")

    #obtener lista de tickers disponibles para visualizar
    tickers = get_tickers_disponibles()

    if len(tickers) == 0:
        print("Ticker no disponible en base de datos. Reinicie programa y actualice")
        return

    if opcion2 == "1":
        #mostrar resumen de consultas
        print("Mostrando resumen: ")
        mostrar_consultas()
    elif opcion2 == "2":
        #mostrar tickers disponibles y crear gráfico
        print("Tickers disponibles:")
        for i in tickers:
            print(i[0])
        print(" ")
        ticker_elegido = input("Elija ticker a graficar: ")
        crear_grafico(ticker_elegido)
        print(" ")
    else:
        print("Opción incorrecta. Terminando el programa")

#para control de ejecución
if __name__ == "__main__":
    main()
