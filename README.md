## Certificacion-Profesional-Python

Trabajo Final de curso de Pyhton inicial dictado por ITBA en Q4 2023.

### Requisitos previos

Tener Python instalado en el sistema. Se puede descargar desde <https://www.python.org/>.
Versión utilizada: **Python 3.10.9**.

### Instalación de dependencias

Las dependencias necesarias se ubican en el archivo **requirements.txt**.
Pueden instalarse con este comando:*pip install -r requirements.txt*.

### Ejecución del programa

En consola Windows PowerShell, por ejemplo, se puede ejecutar el programa por medio de este comando: *python tp_final.py*.

### Configuración de API Key

La API Key se puede obtener creando una cuenta en este sitio: <https://polygon.io/docs/stocks/getting-started>. Luego, reemplazarla en la *línea 13* del código **tp_final.py**. 

### Elección de ticker a consultar

En el archivo **ejemplos_tickers.txt** se ubican ejemplos de tickers que pueden consultarse en el programa. Se consulta un rango de fechas comprendido entre *fecha_inicio = AAAA-MM-DD* y *fecha_fin = AAAA-MM-DD**, por lo que la mínima granularidad de información es por día. 

### Interpretación de gráficos

El programa brinda 2 gráficos evolutivos:

* Gráfico de velas: evolución diaria de precios del ticker consultado. 

⋅⋅⋅Cada vela se dibuja con el precio de apertura, el precio de cierre (especificado con "c"), el precio mínimo y el precio máximo alcanzado en el día. Si la vela es verde, significa que el precio de cierre fue mayor al precio de apertura; caso contrario, la vela será roja. 

* Gráfico de barras: evolución diaria de volumen del ticker consultado.

⋅⋅⋅Cada barra indica la cantidad de acciones que se negociaron por día.

### Observaciones

* Es necesario que exista información del ticker a visualizar en la base de datos. Para ello, siempre se debe comenzar por la opción de *Actualización de datos* y especificar el ticker a consultar junto con su rango de fechas.

* Si se realizan varias consultas de un mismo ticker, con fechas muy aisladas entre sí, es probable que los gráficos resulten difíciles de interpretar. De ser el caso, se puede eliminar la info de 'base_de_datos.db' y volver a realizar las consultas deseadas.