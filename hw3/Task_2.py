"""создать список из 100 элементов, случайные числа от -50 до 50,
записать в файл "numbers.txt" положительные элементы считать числа из файла посчитать среднее арифметическое"""

from random import randint

list_1 = [randint(-50, 50) for i in range(100)]
with open('numbers.txt', 'w') as f:
    for number in list_1:
        if number > 0:
            f.write(f'{number}\n')

with open('numbers.txt', 'r') as f:
    lines = f.readlines()
    count = 0
    list_2 = []
    for line in lines:
        list_2.append(int(line))
        count += 1
    print(count)
    print(sum(list_2) / count)
