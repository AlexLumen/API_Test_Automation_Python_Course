""" создать список из 50 случайных чисел от 10 до 40. найти все числа, которые делятся на 2 и 5 без остатка"""
from random import randint

list_1 = [randint(10, 40) for i in range(50)]
list_2 = []
for item in list_1:
    if item % 2 == 0 and item % 5 == 0:
        list_2.append(item)
print(list_2)
