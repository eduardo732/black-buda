import datetime
import pytz

def calcular_timestamp():
    # Crear un objeto de zona horaria para GMT-03:00
    zona_horaria = pytz.timezone('America/Argentina/Buenos_Aires')

    # Crear un objeto datetime para el 1 de marzo de 2024 a las 12:00 en la zona horaria especificada
    fecha = datetime.datetime(2024, 3, 1, 12, 0, 0, tzinfo=zona_horaria)

    # Obtener el timestamp para esa fecha y hora
    timestamp_inicio = fecha.timestamp()

    # Sumar una hora para obtener el timestamp del final del intervalo (entre las 12:00 y las 13:00)
    fecha_final = fecha + datetime.timedelta(hours=1)
    timestamp_final = fecha_final.timestamp()

    return timestamp_inicio, timestamp_final
