"""создайте функцию для определение гипотенузы если заданы катеты в аргументах"""
from math import sqrt


def hypotenuse(a, b):
    """Функция определения гипотенузы по известным катетам треугольника"""
    return sqrt(a**2 + b**2)
