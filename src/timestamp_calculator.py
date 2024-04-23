import datetime
import pytz

def calcular_timestamp():
    zona_horaria = pytz.timezone('America/Santiago')
    fecha = datetime.datetime(2024, 3, 1, 12, 0, 0, tzinfo=zona_horaria)
    timestamp_inicio = int(fecha.timestamp() * 1000)
    fecha_final = fecha + datetime.timedelta(hours=1)
    timestamp_final = int(fecha_final.timestamp() * 1000)
    return timestamp_inicio, timestamp_final
