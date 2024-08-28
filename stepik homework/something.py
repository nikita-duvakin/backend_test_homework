import math

n = float(input())
a = float(input())

S = (n * (a ** 2)) / (4 * math.tan(math.pi / n))
print(S)
