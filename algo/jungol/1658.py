# 1658 최대공약수와 최소공배수

from sys import stdin
input = stdin.readline

x, y = map(int, input().split())

g = 1
for i in range(1, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
        g = i

a = x // g
b = y // g

print(g)
print(g * a * b)
