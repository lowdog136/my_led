# Вызовите библиотеку функций, которая может вызвать модуль DHT
import Adafruit_DHT
 # библиотека времени должна использовать функцию задержки sleep () внутри
import time

 # Объявить сенсорный объект
sensor = Adafruit_DHT.DHT22
 # Если это модуль DHT22, напишите DHT22
# sensor = Adafruit_DHT.DHT22
 # Используйте Raspberry Pi pin 4
pin = 4 #GPIO4

 # Цикл измерения температуры 10 раз
for i in range(1):
         # Используйте датчик для определения влажности (ч) и температуры (т)
    h, t = Adafruit_DHT.read_retry(sensor, pin)
         # Если есть проблема с полученной температурой или влажностью, она не будет выведена, и она будет выведена, если нет проблемы.
    if h is not None and t is not None and t > -271 and t < 100:
        print('Температура = {}°C  Влажность = {}%'.format(t, h))
    else:
        print('Failed to get data.')
         # Задержка 1 секунда
    time.sleep(1)
