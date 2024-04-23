import requests
from utils import calculate_timestamp_today, calculate_timestamp_a_year_ago

def get_info_today():
	timestamp_twelve, timestamp_thirteen = calculate_timestamp_today()
	return _info(timestamp_twelve, timestamp_thirteen)

def get_info_a_year_ago():
	timestamp_twelve, timestamp_thirteen = calculate_timestamp_a_year_ago()
	return _info(timestamp_twelve, timestamp_thirteen)

def _info(timestamp_twelve, timestamp_thirteen):
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
    return [entry for entry in entries if int(entry[0]) >= timestamp_twelve]