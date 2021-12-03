"""создайте функцию для вычисление евклидово расстояние"""
from math import sqrt


def distance(p, q):
    return sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
