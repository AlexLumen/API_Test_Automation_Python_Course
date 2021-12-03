# -*- coding: utf-8 -*-
"""создать класс Wolf с атрибутами: скорость, вес, цвет - добавить к классу Wolf метод get_power,
 возвращающий мощность power = speed**2 / weight - создать 100 объектов класса Wolf исходные значение
  взять рандомно из диапазона значений - найти самого сильного волка из списка
speed in range(20, 200)

weight in range(30, 70)

color = ['white', 'black', 'gray', 'ginger', 'brown']"""
from random import *

colors = ['white', 'black', 'gray', 'ginger', 'brown']


class Wolf:
    def __init__(self, speed, weight, color):
        self.speed = speed
        self.weight = weight
        self.color = color

    def __lt__(self, other):
        return self.get_power() < other.get_power()

    def __gt__(self, other):
        return self.get_power() > other.get_power()

    def get_power(self):
        return self.speed ** 2 / self.weight


wolfs = [Wolf(randint(30, 70), randint(20, 200), choice(colors)) for i in range(100)]

print(max(wolfs))
