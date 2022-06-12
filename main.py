"""программа, которая находит вещественные корни квадратного уравнения"""
import math
from math import *
a, b, c = float(input()), float(input()), float(input())
d = (b ** 2) - (4 * a * c)

x1 = (-b + (d ** 0.5)) / (2 * a)
x2 = (-b - (d ** 0.5)) / (2 * a)

# если меньше 0
if d < 0:
    print("Нет корней")

# если равен 0
elif d == 0:
    print(-b / (2 * a))

# если больше 0
elif d > 0:
    print(min(x1, x2))
    print(max(x1, x2))
    print(___________)
