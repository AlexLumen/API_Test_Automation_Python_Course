# -*- coding: utf-8 -*-
"""создать класс Wolf с атрибутами: скорость, вес, цвет - добавить к классу Wolf метод get_power,
 возвращающий мощность power = speed**2 / weight - создать 100 объектов класса Wolf исходные значение
  взять рандомно из диапазона значений - найти самого сильного волка из списка
speed in range(20, 200)

weight in range(30, 70)

color = ['white', 'black', 'gray', 'ginger', 'brown']"""
from random import *


class Wolf:
    speed = 0
    weight = 0
    color = []

    def get_power(self):
        return self.speed ** 2 / self.weight


wolfs = []
for i in range(100):
    wolf = Wolf()
    wolf.speed = randint(20, 200)
    wolf.weight = randint(30, 70)
    wolf.color = choice(['white', 'black', 'gray', 'ginger', 'brown'])
    power_wolf = wolf.get_power()
    wolfs.append([wolf.speed, wolf.weight, wolf.color, power_wolf])

powers = []
powerfull_wolf = []
for wolf in wolfs:
    powers.append(wolf[3])
    if max(powers) in wolf:
        powerfull_wolf = wolf

print(f'Самый сильный волк:Скорость - {powerfull_wolf[0]}, Вес - {powerfull_wolf[1]}, Цвет - {powerfull_wolf[2]},'
      f'Сила - {powerfull_wolf[3]}')
