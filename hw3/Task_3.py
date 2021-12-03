""" создать список слов из 1000 элементов, получить слова из списка words рассчитать вероятность для каждого слова
words =['hello', 'python', 'good', 'car', 'bye', 'sleep', 'python', 'car', 'python']"""



import random

words = ['hello', 'python', 'good', 'car', 'bye', 'sleep', 'python', 'car', 'python']
new_words = [random.choice(words) for i in range(0, 1000)]
probability = {}
for word in words:
    probability.update({word: round(words.count(word) / len(words) * 100, 2)})
print(f'Вероятность каждого слова: {probability}')




