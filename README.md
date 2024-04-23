# Título del Proyecto

Black Buda

## Descripción

El desafío consiste en obtener datos de la api pública de buda...
BlackBuda
Imagina que el 1 de marzo de 2024, en el lapso de una hora, de 12:00 a 13:00, Buda.com lanzó una oferta especial llamada BlackBuda. Durante este período, ¡todos los usuarios que operaran en el mercado BTC-CLP disfrutaron de un asombroso 100% de descuento en las comisiones de transacción! 

Fue una oportunidad increíble para comprar y vender bitcoin  y ahora necesitamos de tu ayuda para evaluar el desempeño del BlackBuda.

Utilizando nuestra API pública, necesitamos que recopiles la información necesaria para analizar las siguientes situaciones. 

Supuestos:
Las comisiones se cobran en CLP.
Para todos los cálculos utilizar el horario entre 12:00 y 13:00, ambos inclusive, considera la zona horaria GMT -03:00.
Para todas las respuestas truncar en 2 decimales, ocupando un punto como separador de decimales.
Recuerda que en un mercado del tipo Moneda_1-Moneda_2, la cantidad transada está en Moneda_1 y el precio en Moneda_2.

### Desafío 1
¿Cuánto dinero (en CLP) se transó durante el evento "Black Buda" BTC-CLP ? (truncar en 2 decimales)

### Desafío 2
En comparación con el mismo día del año anterior, ¿cuál fue el aumento porcentual en el volumen de transacciones (en BTC)? (truncar en 2 decimales)

### Desafío 3
Considerando que la comisión normal corresponde a un 0.8% ¿Cuánto dinero (en CLP) se dejó de ganar debido a la liberación de comisiones durante el BlackBuda? (truncar en 2 decimales)

Para solucionar estos desafíos decidí dividir la lógica en distintos archivos:
-src/utils : Este archivo se creó con la finalidad de obtener la fecha solicitada en timestamp milisegundos.
-src/test_timestamp : Decidí asegurarme que el timestamp fuese correcto, por lo que le apliqué test a la lógica.
-src/request: Aquí dejé la lógica para obtener la información que necesitaba
-src/exercise: Aquí separé la lógica dependiendo del desafío que necesitaba
-src/index: Aquí es donde se escriben las respuestas de los desafíos por lo que debes correr este script para saberlo!

## Requisitos
Python 3.9 o superior

## Como ejecuto el script
python .\index.py

## Como corro el test
python .\test_timestamp.py