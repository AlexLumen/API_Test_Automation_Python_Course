"""дано число, если больше 100 выведите «more», если в диапазоне 10-100 выведите «mid», иначе выведите «low»"""

number = int(input())

if number > 100:
    print("more")
elif 10 <= number <= 100:
    print("medium")
else:
    print("low")
