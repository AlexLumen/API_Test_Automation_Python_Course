"""создать словарь из 5 элементов, значения - случайный список из 10 чисел, найти суммы всех списков"""
from random import randint

di = {key: randint(1, 10) for key in range(5)}
print(sum(di.values()))
