## Explicación de la estructura de este código

El archivo principal tp_final.py presenta funciones principales para gestionar la interacción con el usuario de manera clara y amigable:
- `print_menu()`
- `actualizar_datos()`
- `visualzar_datos()`

A su vez, dicho archivo se compone de otras funciones localizadas en otros archivos:
- `get_finanzas.py`
- `crear_tabla_finanzas.py`
- `crear_tabla_consultas.py`
- `escribir_tabla_consultas.py`
- `escribir_nuevo_registro.py`
- `mostrar_consultas.py`
- `crear_grafico.py`
- `get_tickers_disponibles.py`

Esta modularidad facilita la comprensión del código y permite realizar cambios en secciones específicas, sin afectar al resto del programa. Cada función tiene una responsabilidad específica y realiza una tarea definida.

Para controlar la ejecución, se usa `if __name__ == "__main__":`, lo cual asegura que el programa principal `main()` se ejecute cuando el script se ejecuta directamente y no cuando se importa como módulo (buena práctica).


### main()

La función `main()` se encarga de imprimir el menú principal y de preguntarle al usuario si desea realizar una actualización de datos ingresando 1 o si desea visualizar datos ingresando 2. En caso de que se ingresen valores distintos, saldrá mensaje de opción incorrecta. Luego de cada acción, el usuario podrá realizar otra operación o podrá salir del programa presionando la tecla `s`.


### actualizar_datos()

La función `actualizar_datos()` utiliza varias funciones: 

- la función `crear_tabla_finanzas()` crea una tabla llamada tabla_finanzas en una base de datos SQLite, si esa tabla aún no existe, y define la estructura de la tabla con columnas específicas para almacenar datos financieros.

- la función `crear_tabla_consultas()` crea una tabla llamada tabla_consultas en una base de datos SQLite, si esa tabla aún no existe, y defina la estructura de la tabla con 3 columnas: ticker, fecha_inicio y fecha_fin.

- la función `get_finanzas()` realiza una solicitud a la API de Polygon para obtener datos financieros de un activo (ticker) en un rango de fechas específico, y devuelve estos datos en formato JSON. También maneja errores en la solicitud y decodificación JSON.

- la función `escribir_nuevo_registro()` inserta nuevos registros en tabla_finanzas anteriormente creada, utilizando los datos proporcionados por la respuesta de la API para un rango de fechas específico.

- la función `escribir_tabla_consultas()` inserta nuevos registros en tabla_consultas anteriormente creada.Cada vez que el usuario realice una consulta sobre un ticker específico en un rango de fechas específico, se registra esa información en tabla_consultas. 

En definitiva, la función `actualizar_datos()` se encarga de la actualización de datos financieros. Para ello le solicita al usuario que ingrese ticker de interés junto con el rango de fechas deseado, realiza una solicitud a la API para obtener esos datos, y actualiza las tablas con la info obtenida. Además, maneja errores por medio del bloque try-except y cierra la conexión a la base de datos SQLite.


### visualizar_datos()

Por otro lado, la función `visualizar_datos()` utiliza otras funciones:

- la función `get_tickers_disponibles()` brinda el listado de tickers únicos que se encuentran en la tabla_finanzas.

- la función `mostrar_consultas()` brinda los registros almacenados en tabla_consultas, lo cual es útil para mostrarle al usuario las consultas que ha realizado, proporcionándole tickers y fechas de inicio/fin.

- la función `crear_grafico()` toma un ticker como entrada, recupera los datos relacionados a ese ticker de la base de datos, y crea 2 gráficos: uno de velas con parámetros de precios, y otro de barras con parámetro de volumen. 

En definitiva, la función `visualizar_datos()` le proporciona al usuario una interfaz simple para que seleccione qué tipo de visualización desea realizar: un resumen de consultas realizadas o gráficos para un ticker específico. 


### Conclusiones

- El programa desarrollado está estructurado de manera modular para facilitar su lectura, prueba y mantenimiento.

- Cada archivo se encarga de una tarea específica, lo cual sigue el principio de "separación de preocupaciones" y facilita la comprensión y el mantenimiento.

- Cada función realiza una tarea específica, lo que facilita pruebas individuales y lectura.

- El menú interactivo proporciona una interfaz de usuario amigable, aunque quizás sería útil agregar más información sobre cómo interactuar con el programa. 

- Se manejan excepciones en lugares específicos para mejorar la robustez del programa al gestionar posibles errores. 

- Se han comentado líneas principales para explicar funcionalidades. 

- Se define la key de la API como constante global, aunque se podrían implementar mejores prácticas de seguridad para cifrarla. 













