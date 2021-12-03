# -*- coding: utf-8 -*-
"""создайте функцию print_triangle, которая принимает число и выводит следующий шаблон, например для n=5"""


def print_triangle(number):
    for i in range(number):
        print("")
        for j in range(1, 6 - i):
            print(j, end=" ")
    print("\n")
