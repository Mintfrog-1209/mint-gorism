# 1629 곱셈 (23/03/16)
from sys import stdin
input = stdin.readline

A, B, C = map(int, input().split())

def multi(x, y, z):
    if y == 1:
        return x%z
    elif y % 2 == 0:
        return multi(x, y//2, z) ** 2 % z
    else:
        return multi(x, y//2, z) ** 2 * x % z

print(multi(A, B, C))