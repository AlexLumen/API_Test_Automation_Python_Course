"""создайте функцию для нахождение корней квадратного уравнения"""
from math import sqrt


def quadratic_roots(a, b, c):
    """Функция нахождения корней квадратного уровнения полного и неполного"""
    d = (b ** 2) - (4 * a * c)
    if a != 0 and b != 0 and c != 0:
        if d > 0:
            return (-b + sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)
        elif d == 0:
            return -b / (2 * a)
        else:
            return "Действительных корней нет"
    elif a != 0 and b != 0 and c == 0:
        return 0, -b / a
    elif a != 0 and b == 0 and c != 0:
        return -(-c / a), (-c / a)
    elif a == 0 and b != 0 and c != 0:
        return -c / b
    elif a == 0 and b == 0 and c != 0:
        return "Действительных корней нет"
    else:
        return 0
