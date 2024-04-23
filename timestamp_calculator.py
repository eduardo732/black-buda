import datetime
import pytz

def calcular_timestamp():
    zona_horaria = pytz.timezone('America/Argentina/Buenos_Aires')
    fecha = datetime.datetime(2024, 3, 1, 12, 0, 0, tzinfo=zona_horaria)
    timestamp_inicio = fecha.timestamp()
    fecha_final = fecha + datetime.timedelta(hours=1)
    timestamp_final = fecha_final.timestamp()
    return timestamp_inicio, timestamp_final
