import datetime
import pytz

def calculate_timestamp_today():
    date = get_date(2024) 
    timestamp_init = int(date.timestamp() * 1000)
    fecha_final = date + datetime.timedelta(hours=1)
    timestamp_final = int(fecha_final.timestamp() * 1000)
    return timestamp_init, timestamp_final

def calculate_timestamp_a_year_ago():
    date = get_date(2023) 
    timestamp_init = int(date.timestamp() * 1000)
    fecha_final = date + datetime.timedelta(hours=1)
    timestamp_final = int(fecha_final.timestamp() * 1000)
    return timestamp_init, timestamp_final
    
def get_date(year):
    timezone = pytz.timezone('America/Santiago')
    return datetime.datetime(year, 3, 1, 12, 0, 0, tzinfo=timezone)