import time
import requests
from timestamp_calculator import calcular_timestamp

timestamp_inicio, timestamp_final = calcular_timestamp()

print("Timestamp de inicio:", timestamp_inicio)
print("Timestamp de finalización:", timestamp_final)


market_id = 'btc-clp'
url = f'https://www.buda.com/api/v2/markets/{market_id}/trades'
response = requests.get(url, params={
    'timestamp': timestamp_inicio,
    'limit': 50,
})
print(response.json())
