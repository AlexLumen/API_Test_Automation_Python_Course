"""введите из консоли длину и ширину дома, рассчитайте площадь, если площадь больше 100, напечатайте «большой дом»,
    иначе выведите «маленький дом»"""
length = int(input())
width = int(input())

if length * width > 100:
    print("большой дом")
else:
    print("маленький дом")