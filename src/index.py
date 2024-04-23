import time
import requests
from timestamp_calculator import calcular_timestamp

timestamp_twelve, timestamp_thirteen = calcular_timestamp()

print("Timestamp de inicio:", timestamp_twelve)
print("Timestamp de finalización:", timestamp_thirteen)


market_id = 'btc-clp'
url = f'https://www.buda.com/api/v2/markets/{market_id}/trades'
response = requests.get(url, params={
    'timestamp': timestamp_thirteen,
    'limit': 70,
})

if response.status_code != 200:
    print("Error al realizar la solicitud:", response.status_code)

data = response.json()
timestamp = data['trades']['timestamp']
last_timestamp = data['trades']['last_timestamp']
market_id = data['trades']['market_id']
entries = data['trades']['entries']
entries_filtradas = [entry for entry in entries if int(entry[0]) > timestamp_twelve]
#1709311380000
print(entries_filtradas)