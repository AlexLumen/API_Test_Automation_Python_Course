# -*- coding: utf-8 -*-
"""создать классы Nokia, Iphone, Samsung, унаследованные от класса Phone аргументы в конструтурах классов:
 Phone - color, price, name Nokia - color, price, count_buttons Samsung - color, price, waterproofness
 Iphone - color, price, speed_internet в нижеприведенном блоке создается 120 объектов класса Iphone,
  105 объектов класса Samsung,
  75 объектов класса Nokia, запустить этот код и убедиться что все классы правильно определны
from random import *
colors = ["red", "black", "white", "golden", "silver"]
speed_internet = ["2G", "3G", "4G", "5G"]
waterproofness = [True, False]
list_Iphone = [Iphone(choice(colors), randint(15000, 110000), choice(speed_internet)) for i in range(120)]
list_Sam = [Samsung(choice(colors), randint(8000, 90000), choice(waterproofness)) for i in range(105)]
list_Nokia = [Nokia(choice(colors), randint(3000, 25000), randint(24, 56)) for i in range(75)]"""
from random import *

colors = ["red", "black", "white", "golden", "silver"]
speed_internet = ["2G", "3G", "4G", "5G"]
waterproofness = [True, False]


class Phone:

    def __init__(self, color, price, name):
        self.color = color
        self.price = price
        self.name = name


class Nokia(Phone):
    def __init__(self, color, price, count_buttons):
        super().__init__(color, price, "Nokia")
        self.count_buttons = count_buttons


class Samsung(Phone):
    def __init__(self, color, price, waterproofness):
        super().__init__(color, price, "Samsung")
        self.waterproofness = waterproofness


class Iphone(Phone):
    def __init__(self, color, price, speed_internet):
        super().__init__(color, price, "Iphone")
        self.speed_internet = speed_internet


list_Iphone = [Iphone(choice(colors), randint(15000, 110000), choice(speed_internet)) for i in range(120)]
list_Sam = [Samsung(choice(colors), randint(8000, 90000), choice(waterproofness)) for i in range(105)]
list_Nokia = [Nokia(choice(colors), randint(3000, 25000), randint(24, 56)) for i in range(75)]
