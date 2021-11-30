# -*- coding: utf-8 -*-
""" создать функцию my_sqrt, которая вычисляет квадратный корень из числа, если число меньше нуля,
 поднимает исключение ValueError с сообщением "impossible to got negative number"""


def my_sqrt(n):
    if n < 0:
        raise ValueError("impossible to got negative number")
    return n ** 0.5
