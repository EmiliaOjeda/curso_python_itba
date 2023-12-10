import requests
import json

def get_finanzas (ticker, fecha_inicio, fecha_fin, api_key):
    response = requests.get (f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{fecha_inicio}/{fecha_fin}?apiKey={api_key}")
    response = response.json ()
    print (json.dumps(response, indent = 4))
    return response