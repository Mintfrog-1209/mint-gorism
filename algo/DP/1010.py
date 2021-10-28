# 1010 다리 놓기
from sys import stdin
input = stdin.readline

t = int(input())


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


for i in range(t):
    n, m = map(int, input().split())
    if m == n:
        print(1)
    else:
        print(factorial(m)//factorial(m-n)//factorial(n))
