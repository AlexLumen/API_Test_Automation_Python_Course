"""создать функции area, circumference, volume каждая из них принимает аргумент радиус
создать эти функции через четвертую функцию wrapper которая возвращает lambda функцию
посмотрите на формулы каждой функции, найдите общее чтоб могли определять все 3 функции в одном wrapper

area = math.pi * radius ** 2

circumference = 2 * math.pi * radius

volume = 4/3 * math.pi * radius ** 3"""
import math


def wrapper(radius):
    return lambda arg1, arg2: arg1 * math.pi * radius ** arg2


def area(radius):
    are = wrapper(radius)
    return are(1, 2)


def circumference(radius):
    cicrum = wrapper(radius)
    return cicrum(2, 1)


def volume(radius):
    vol = wrapper(radius)
    vol(4/3, 3)
    return vol(4/3, 3)
