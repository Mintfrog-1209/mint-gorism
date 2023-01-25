# 1692 곱셈

from sys import stdin
input = stdin.readline

x = int(input())
y = int(input())

z1 = x * (y % 10)
z2 = (x * (y % 100) - z1) // 10
z3 = x * (y // 100 )
z4 = x * y
print(z1)
print(z2)
print(z3)
print(z4)
