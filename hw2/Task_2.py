"""введите из консоли слово, если длина больше 5 символов, выведите три буквы посередине"""

word = input()
median_char = len(word) // 2 - 1
print(median_char)
if len(word) > 5:
    print(word[median_char:median_char + 3])
