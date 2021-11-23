"""Русское лото у вас есть список из 4 чисел (например 4, 78, 99, 872) создаете бесконечный цикл
в котором генерируется случайное число в диапазоне от 0 до 1000 остановить цикл тогда,
когда выпадут все числа из нашего билета, посчитать количество попыток"""
from random import randint

bilet_numbers = [randint(0, 1000) for i in range(4)]


count = 0
numbers_loto = []
for item in bilet_numbers:
    while item not in numbers_loto:
        count += 1
        num = randint(0, 1000)
        numbers_loto.append(num)

print(count)
