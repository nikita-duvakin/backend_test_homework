a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c
x_1 = (-b - D ** 0.5) / (2 * a)
x_2 = (-b + D ** 0.5) / (2 * a)
x_3 = -b / (2 * a)

if D > 0:
    print(min(x_1, x_2))
    print(max(x_1, x_2))
elif D == 0:
    print(x_3)
else:
    print('Нет корней')