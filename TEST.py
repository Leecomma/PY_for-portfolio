"""Самописный калькулятор"""
a = int(input())
b = int(input())

print("Уточните операцию + - * /")

c = input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif b == 0 and c == "/":
    print("На ноль делить нельзя!")
elif c == "/":
    print(a / b)
else:
    print("Неверная операция")