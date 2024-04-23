import unittest
import datetime
import pytz
from utils import calculate_timestamp_today, calculate_timestamp_a_year_ago


class TestCalcularTimestamp(unittest.TestCase):
    def test_calculo_timestamp_today(self):
        timestamp_inicio, timestamp_final = calculate_timestamp_today()

        fecha_inicio = datetime.datetime.fromtimestamp(timestamp_inicio / 1000, tz=pytz.timezone('America/Santiago'))
        fecha_final = datetime.datetime.fromtimestamp(timestamp_final / 1000, tz=pytz.timezone('America/Santiago'))

        self.assertEqual(fecha_inicio, datetime.datetime(2024, 3, 1, 12, 0, 0, tzinfo=pytz.timezone('America/Santiago')))
        self.assertEqual(fecha_final, datetime.datetime(2024, 3, 1, 13, 0, 0, tzinfo=pytz.timezone('America/Santiago')))

    def test_calculo_timestamp(self):
        timestamp_inicio, timestamp_final = calculate_timestamp_a_year_ago()

        fecha_inicio = datetime.datetime.fromtimestamp(timestamp_inicio / 1000, tz=pytz.timezone('America/Santiago'))
        fecha_final = datetime.datetime.fromtimestamp(timestamp_final / 1000, tz=pytz.timezone('America/Santiago'))

        self.assertEqual(fecha_inicio, datetime.datetime(2023, 3, 1, 12, 0, 0, tzinfo=pytz.timezone('America/Santiago')))
        self.assertEqual(fecha_final, datetime.datetime(2023, 3, 1, 13, 0, 0, tzinfo=pytz.timezone('America/Santiago')))

if __name__ == '__main__':
    unittest.main()
