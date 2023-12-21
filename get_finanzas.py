import requests
#import json

'''
Se realiza solicitud a API de Polygon para obtener datos financieros.

Parámetros:
- ticker (str): símbolo del activo financiero
- fecha_inicio (str): fecha de inicio en formato 'AAAA-MM-DD'
- fecha_fin (str): fecha de fin en formato 'AAAA-MM-DD'
- api_key (str): clave de API para acceder a API de Polygon

Devuelve objeto JSON con datos financieros.

'''

def get_finanzas(ticker, fecha_inicio, fecha_fin, api_key):

    try:
        #construir URL para solicitud a API
        url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{fecha_inicio}/{fecha_fin}?apiKey={api_key}"
        #realizar solicitud GET a API y obtener respuesta
        response = requests.get(url)
        #verificar si hay errores en solicitud
        response.raise_for_status()  

        #imprimir objeto JSON antes de devolverlo
        json_data = response.json()
        #print(json.dumps(json_data, indent=4))

        #devolver el objeto JSON de la respuesta
        return json_data

    #manejar excepciones para posibles errores durante solicitud o procesamiento JSON
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud a la API: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar la respuesta JSON: {e}")
        return None